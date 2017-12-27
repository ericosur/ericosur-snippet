#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <string>
#include <iostream>
#include <fstream>
#include <json.hpp>

#define CURL_STATICLIB
#include <curl/curl.h>

#define DEFAULT_OUT_JSON    "/tmp/out.json"

struct MemoryStruct {
  char *memory;
  size_t size;
};

using namespace std;
using namespace nlohmann;

string remove_quote(const string& input_string)
{
    std::string str1 = input_string;
    str1.erase(std::remove(str1.begin(), str1.end(), '\"'),
               str1.end());
    //std::cout << str1 << '\n';

    return str1;
}

string get_query_string(const string& city)
{
#define QUERY_STR "https://query.yahooapis.com/v1/public/yql?" \
    "q=select+%2A+from+weather.forecast+where+woeid+in+%28+" \
    "select+woeid+from+geo.places+%28+1+%29+where+text+%3D+%22+"
#define QUERY_STR2    "+%22+%29+and+u+%3D+%22+c+%22&format=json"

    string result = string(QUERY_STR) + city + string(QUERY_STR2);
    //cout << "query string:" << result << endl;

    return result;
}

size_t write_callback(char *ptr, size_t size, size_t nmemb, void *userdata)
{
    size_t realsize = size * nmemb;
    struct MemoryStruct *mem = (struct MemoryStruct *)userdata;

    mem->memory = (char*)realloc(mem->memory, mem->size + realsize + 1);
    if(mem->memory == NULL) {
       /* out of memory! */
        printf("not enough memory (realloc returned NULL)\n");
        return 0;
    }

    memcpy(&(mem->memory[mem->size]), ptr, realsize);
    mem->size += realsize;
    mem->memory[mem->size] = 0;

    return realsize;
}

void write_chunk_to_my_file(MemoryStruct* pChunk, const char* fname)
{
    FILE* fptr = NULL;
    if ( (fptr = fopen(fname, "wb")) == NULL ) {
        fprintf(stderr, "failed to open file to write\n");
        return;
    }
    size_t byte_wrote = fwrite(pChunk->memory, sizeof(char), pChunk->size, fptr);
    if (byte_wrote != pChunk->size) {
        fprintf(stderr, "something wrong, wrote %ld but request %ld\n",
                byte_wrote, pChunk->size);
    }
    fclose(fptr);
    printf("output json to: %s\n", fname);
}

void read_json_elements(const json& jj)
{
    //cout << __func__ << endl;
    try {
        if (jj.at("query").at("results").is_null()) {
            cout << "[ERR] the query is null" << endl;
            return ;
        }

        json foo = jj.at("query").at("results").at("channel");
        cout << "city:" << foo.at("location").at("city") << endl;
        cout << "text:" << foo.at("item").at("condition").at("text") << endl;
        string temp = remove_quote(foo.at("item").at("condition").at("temp"));
        string unit = remove_quote(foo.at("units").at("temperature"));
        string deg = "\xC2\xB0";    // degree symbol
        string result = temp + deg + unit;
        cout << "temp:" << result << endl;
    } catch (json::parse_error& e) {
        cout << "parse error:" << e.what() << endl;
    } catch (json::out_of_range& e) {
       std::cout << "out of range:" << e.what() << '\n';
    }
}
void read_json_from_file(const char* fname)
{
    try {
        ifstream inf(fname);
        json jj;
        inf >> jj;
        read_json_elements(jj);

    } catch (json::parse_error& e) {
        cout << "parse error:" << e.what() << endl;
    } catch (json::out_of_range& e) {
       std::cout << "out of range:" << e.what() << '\n';
    }
}

void read_json_from_memory(const char* ptr)
{
    try {
        json jj = json::parse(ptr);
        read_json_elements(jj);
    } catch (json::parse_error& e) {
        cout << "parse error:" << e.what() << endl;
    } catch (json::out_of_range& e) {
       std::cout << "out of range:" << e.what() << '\n';
    }
}

int query_weather(const string& city)
{
    CURL *curl;
    CURLcode res;

    struct MemoryStruct chunk;

    chunk.memory = (char*)malloc(1);  /* will be grown as needed by the realloc above */
    chunk.size = 0;    /* no data at this point */

    curl_global_init(CURL_GLOBAL_ALL);

    curl = curl_easy_init();
    if (curl)
    {
        string query_string = get_query_string(city);
        //curl_easy_setopt(curl, CURLOPT_URL, "https://google.com");
        curl_easy_setopt(curl, CURLOPT_URL, query_string.c_str());
        /* could be redirected, so we tell LibCurl to follow redirection */
        curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
        // setup a write callback function
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);

        /* we pass our 'chunk' struct to the callback function */
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);

        /* some servers don't like requests that are made without a user-agent
         field, so we provide one */
        curl_easy_setopt(curl, CURLOPT_USERAGENT, "libcurl-agent/1.0");

        /* Perform the request, res will get the return code */
        res = curl_easy_perform(curl);

        cout << "query weather for " << city << " =====>" << endl;
        /* Check for errors */
        if (res != CURLE_OK) {
            fprintf(stderr, "[ERR] curl_easy_perform() failed: %s (%d)\n", curl_easy_strerror(res), res);
            fprintf(stderr, "[ERR] will read from a previous file: %s\n", DEFAULT_OUT_JSON);
            read_json_from_file(DEFAULT_OUT_JSON);
        } else {
            /*
             * Now, our chunk.memory points to a memory block that is chunk.size
             * bytes big and contains the remote file.
             *
             * Do something nice with it!
             */
            //printf("%lu bytes retrieved\n", (long)chunk.size);
            write_chunk_to_my_file(&chunk, DEFAULT_OUT_JSON);
            read_json_from_memory(chunk.memory);
        }
    }

    /* Always cleanup */
    curl_easy_cleanup(curl);
    free(chunk.memory);
    curl_global_cleanup();

    return 0;
}


int main(int argc, char* argv[])
{
    if (argc == 1) {
        query_weather("taipei");
    } else {
        for (int i=1; i<argc; ++i) {
            query_weather(argv[i]);
        }
    }

    return 0;
}
