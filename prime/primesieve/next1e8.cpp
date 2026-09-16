//
// g++ -O3 next1e8.cpp -lprimesieve -o next1e8
//
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cerrno>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <fcntl.h>
#include <unistd.h>
#include <primesieve.hpp>

namespace {
const char* output_file = "primes_part2_1e8.txt";
const char* state_file = "next1e8.state";
const char* state_tmp_file = "next1e8.state.tmp";
const char* seed_file = "start_after.seed";  // 新批次起點（最後一個已記錄/驗證過的質數），用後即被消耗
const char* log_file = "next1e8.log";        // 記錄 start/resume/stop 的時間點
const uint64_t total_count = 100000000ULL;   // 每批目標總數，可分多次執行/中斷續跑/新批次
const char* dir_path = ".";

std::string now_timestamp() {
    std::time_t t = std::time(nullptr);
    char buf[32];
    std::strftime(buf, sizeof(buf), "%Y-%m-%d %H:%M:%S", std::localtime(&t));
    return buf;
}

// best-effort event log; a logging failure shouldn't abort an otherwise-good run
void log_line(const std::string& text) {
    FILE* f = std::fopen(log_file, "a");
    if (!f) return;
    std::fprintf(f, "%s %s\n", now_timestamp().c_str(), text.c_str());
    std::fclose(f);
}

void log_event(const char* event, uint64_t count, uint64_t last_prime) {
    char buf[64];
    std::snprintf(buf, sizeof(buf), "%s count=%llu last_prime=%llu",
                  event, (unsigned long long)count, (unsigned long long)last_prime);
    log_line(buf);
}

[[noreturn]] void fail(const std::string& msg) {
    int err = errno;
    std::string full = msg + ": " + std::strerror(err);
    std::cerr << full << "\n";
    log_line("ERROR " + full);
    std::exit(1);
}

// fsyncs the directory itself, otherwise a crash can lose a file's name even if its data was fsynced
void fsync_dir(const char* path) {
    int fd = ::open(path, O_RDONLY | O_DIRECTORY);
    if (fd < 0) fail(std::string("無法開啟目錄以執行 fsync: ") + path);
    if (::fsync(fd) != 0) fail(std::string("fsync 目錄失敗: ") + path);
    ::close(fd);
}

// state file holds "count last_prime"; missing file means no prior progress
bool load_state(uint64_t& count, uint64_t& last_prime) {
    std::ifstream in(state_file);
    if (!in.is_open()) return false;
    in >> count >> last_prime;
    return static_cast<bool>(in);
}

// scans a whole primes file and returns its line count plus the value of its last line
bool read_file_tail(const char* path, uint64_t& total_lines, uint64_t& last_value) {
    FILE* f = std::fopen(path, "rb");
    if (!f) return false;

    std::vector<char> buf(1 << 16);
    std::string current, last_complete_line;
    uint64_t lines = 0;
    size_t n;
    while ((n = std::fread(buf.data(), 1, buf.size(), f)) > 0) {
        for (size_t i = 0; i < n; ++i) {
            char c = buf[i];
            if (c == '\n') {
                ++lines;
                last_complete_line.swap(current);
                current.clear();
            } else {
                current += c;
            }
        }
    }
    std::fclose(f);

    if (lines == 0) return false;
    total_lines = lines;
    last_value = std::strtoull(last_complete_line.c_str(), nullptr, 10);
    return true;
}

// reads a raw prime value from the seed file; returns false if the file doesn't exist
bool read_seed(uint64_t& value) {
    std::ifstream seed(seed_file);
    if (!seed.is_open()) return false;
    seed >> value;
    if (!seed) fail(std::string("種子檔內容無效: ") + seed_file);
    return true;
}

// renames the seed file away once it has been durably used, so a stale value can never be silently re-applied
void consume_seed_file() {
    std::string used = std::string(seed_file) + ".used";
    if (std::rename(seed_file, used.c_str()) != 0) fail("重新命名種子檔失敗");
    fsync_dir(dir_path);
}

// determines where to continue from. Priority: an in-progress checkpoint always resumes as-is (seed
// file ignored for safety); otherwise the current batch is finished (or nothing ever ran), so a seed
// file - if present - starts a fresh batch from that value; this is the only place start_after is decided
void determine_start(uint64_t& count, uint64_t& last_prime, bool& new_batch) {
    new_batch = false;
    uint64_t state_count = 0, state_last_prime = 0;
    bool has_state = load_state(state_count, state_last_prime);

    if (has_state && state_count > 0 && state_count < total_count) {
        count = state_count;
        last_prime = state_last_prime;
        return; // 有未完成的 checkpoint，直接續跑，忽略種子檔
    }

    uint64_t seed_value = 0;
    if (read_seed(seed_value)) {
        count = 0;
        last_prime = seed_value;
        new_batch = true;
        return; // 目前批次已完成（或尚未開始），且提供了種子檔：從種子值開始下一批
    }

    if (has_state) {
        count = state_count;
        last_prime = state_last_prime;
        return; // 批次已完成，且無新種子檔：維持已完成狀態
    }

    if (read_file_tail(output_file, count, last_prime)) return; // 無 checkpoint 但既有輸出檔，採用其最後一行

    fail(std::string("找不到起點：無 checkpoint、無既有輸出檔，且找不到種子檔 ") + seed_file);
}

// fsyncs a regular file's data/size after it was modified outside the normal write path (e.g. truncate)
void fsync_file(const char* path) {
    int fd = ::open(path, O_RDONLY);
    if (fd < 0) fail(std::string("無法開啟檔案以執行 fsync: ") + path);
    if (::fsync(fd) != 0) fail(std::string("fsync 檔案失敗: ") + path);
    ::close(fd);
}

// trims any stray/duplicate lines left after the last completed checkpoint (from a crash mid-write)
// and aborts if the file's checkpoint line doesn't match the state file, since that means real corruption
void repair_output_file(uint64_t count, uint64_t last_prime) {
    FILE* f = std::fopen(output_file, "rb");
    if (!f) fail("無法開啟輸出檔案以檢查一致性");

    std::vector<char> buf(1 << 16);
    std::string last_line;
    uint64_t lines = 0;
    long long offset = 0;
    bool found = false;
    size_t n;

    while (!found && (n = std::fread(buf.data(), 1, buf.size(), f)) > 0) {
        for (size_t i = 0; i < n && !found; ++i) {
            char c = buf[i];
            ++offset;
            if (c == '\n') {
                if (++lines == count) { found = true; break; }
                last_line.clear();
            } else {
                last_line += c;
            }
        }
    }
    std::fclose(f);

    if (!found) fail("輸出檔案行數少於狀態檔記錄，資料不一致，需人工檢查");
    if (std::strtoull(last_line.c_str(), nullptr, 10) != last_prime)
        fail("輸出檔案最後一行與狀態檔記錄的質數不符，資料不一致，需人工檢查");

    if (::truncate(output_file, offset) != 0) fail("截斷輸出檔案失敗");
    fsync_file(output_file);
}

// write -> fsync -> rename -> fsync directory: checkpoint survives a crash, not just a clean exit
void save_state(uint64_t count, uint64_t last_prime) {
    FILE* f = std::fopen(state_tmp_file, "w");
    if (!f) fail("無法開啟狀態暫存檔");
    if (std::fprintf(f, "%llu %llu\n", (unsigned long long)count, (unsigned long long)last_prime) < 0)
        fail("寫入狀態暫存檔失敗");
    if (std::fflush(f) != 0) fail("flush 狀態暫存檔失敗");
    if (::fsync(::fileno(f)) != 0) fail("fsync 狀態暫存檔失敗");
    std::fclose(f);
    if (std::rename(state_tmp_file, state_file) != 0) fail("重新命名狀態檔失敗");
    fsync_dir(dir_path);
}
}

int main() {
    const size_t buffer_size = 65536;           // 批次寫入緩衝區，減少 I/O 開銷

    uint64_t count = 0;
    uint64_t last_prime = 0;
    bool new_batch = false;
    determine_start(count, last_prime, new_batch);
    bool resuming = count > 0 && !new_batch;

    log_event(new_batch ? "NEW_BATCH" : (resuming ? "RESUME" : "START"), count, last_prime);

    if (resuming) repair_output_file(count, last_prime);

    if (count >= total_count) {
        std::cout << "已達目標總數 (" << total_count << ")，無需繼續。\n";
        log_event("STOP", count, last_prime);
        return 0;
    }

    primesieve::iterator it;
    it.jump_to(last_prime + 1);

    bool output_existed = (::access(output_file, F_OK) == 0);
    FILE* out = std::fopen(output_file, "a"); // 一律附加寫入，跨批次持續累積同一份輸出
    if (!out) fail("無法建立輸出檔案");
    if (!output_existed) fsync_dir(dir_path); // 確保新檔案的目錄項目落盤

    bool pending_seed_consumption = new_batch;
    std::string buffer;
    buffer.reserve(buffer_size * 12);

    // durably flushes buffered primes; only after this returns is it safe to advance the checkpoint
    auto flush_buffer = [&]() {
        if (buffer.empty()) return;
        size_t written = std::fwrite(buffer.data(), 1, buffer.size(), out);
        if (written != buffer.size()) fail("寫入輸出檔案失敗（可能磁碟已滿）");
        if (std::fflush(out) != 0) fail("flush 輸出檔案失敗");
        if (::fsync(::fileno(out)) != 0) fail("fsync 輸出檔案失敗");
        buffer.clear();
    };

    uint64_t since_flush = 0;
    for (; count < total_count; ++count) {
        last_prime = it.next_prime();
        buffer += std::to_string(last_prime);
        buffer += '\n';

        if (++since_flush == buffer_size) {
            flush_buffer();
            since_flush = 0;
            save_state(count + 1, last_prime);
            if (pending_seed_consumption) { consume_seed_file(); pending_seed_consumption = false; }
        }
    }

    flush_buffer();
    if (std::fclose(out) != 0) fail("關閉輸出檔案失敗");
    save_state(count, last_prime);
    if (pending_seed_consumption) consume_seed_file();
    log_event("STOP", count, last_prime);

    std::cout << "完成。累計產出總數: " << count << "\n";
    std::cout << "最後一個質數為: " << last_prime << "\n";

    return 0;
}
