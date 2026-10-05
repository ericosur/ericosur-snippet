# 測試圖檔託管與跨平台同步方案建議

本文件針對此專案的圖檔管理需求（主倉庫輕量化、照片私密不公開、跨平台/跨機器自動同步）進行架構分析與方案建議。

---

## 1. 核心需求與背景限制

1. **避免 Git 倉庫膨脹**：測試用圖檔不直接 commit 進目前的 `opencv_python` 程式碼倉庫，保持 Git Clone 與更新時的輕巧快速。
2. **私密性與自有圖片**：使用自己拍攝的風景/靜物照片（無版權風險、可自由裁切調整解析度），**不希望被公開索引或被大眾隨意瀏覽**。
3. **跨平台多環境自動拉取**：在不同作業系統與開發環境中，不需要每次手動傳輸圖檔；腳本執行時自動從遠端同步下載至本地。
4. **替代不穩定的 Imgur**：Imgur 如今會主動阻擋 Python User-Agent（回傳 429/403）、防盜連重定向以及清除舊圖，已不適合作為測試素材圖床。

---

## 2. 方案比較與評估

| 方案 | 隱私性與安全性 | 免費額度 / 成本 | 跨平台設定複雜度 | 適合場景 |
| :--- | :--- | :--- | :--- | :--- |
| **方案 A：獨立私有 GitHub 倉庫 (推薦)** | **高** (Private 權限控管) | 免費 (一般個人帳號均支援) | **低** (開發環境通常已具備 GitHub Token / SSH) | 既有 GitHub 開發者、希望完全私密且零額外服務成本 |
| **方案 B：Cloudflare R2 物件儲存** | **中 ~ 高** (可選 S3 金鑰或未列出長路徑) | 10 GB 儲存免費，**完全免流量費** | **中** (需 Cloudflare 帳號，可免金鑰或使用 `boto3`) | 追求最接近以前 Imgur 的直連體驗，但 100% 自主控管 |
| **方案 C：Cloudinary** | **中** (可設定不公開 listing) | 每月 25 點數 (~25GB 流量與空間) | **低** (直接使用 URL 或官方 SDK) | 原圖很大、希望由雲端自動縮放裁切 (URL 帶參數) |

---

## 3. 方案細節與實作方式

### 方案 A：獨立私有 GitHub Assets 倉庫（最推薦）

在 GitHub 另開一個獨立的 Private 倉庫（例如 `opencv-test-assets`），將裁切優化後的圖檔推送到該倉庫。

* **運作機制**：利用既有的 GitHub Personal Access Token (PAT) 透過 HTTP 標頭拉取 Raw 內容。
* **下載範例 (Python)**：
  ```python
  import os
  import requests

  token = os.getenv("GITHUB_TOKEN")
  headers = {"Authorization": f"token {token}"} if token else {}
  url = "https://raw.githubusercontent.com/<username>/opencv-test-assets/main/photos/deer.png"

  resp = requests.get(url, headers=headers)
  ```
* **優點**：完全與主專案解耦，多環境佈署時只需透過環境變數傳入 Token 即可無縫存取。

---

### 方案 B：Cloudflare R2（S3 相容物件儲存）

Cloudflare R2 最大的優勢在於**完全不收取外網出流量費用（$0 Egress Fee）**。

* **模式 1：Unlisted (未列出/隱密路徑，最貼近 Imgur 舊模式)**
  * 綁定一個不對外公開的自訂子網域或隨機長路徑（例如：`assets-vault.yourdomain.com/secret-hash-9182/deer.png`）。
  * 關閉目錄列表瀏覽（Directory Listing），搜尋引擎無從爬取。
  * 腳本只需發送一般 HTTP GET 即可下載，無須配置 API 金鑰。
* **模式 2：純私有 S3 API**
  * Bucket 設定完全私有，使用 `boto3` 帶入 R2 的 Access Key 與 Secret Key 進行下載。

---

### 方案 C：Cloudinary（動態圖形處理）

適合不想自己在本機先裁切或轉檔的情境：
* 上傳一次高解析度原圖，透過 URL 即時轉換：
  * 原圖：`https://res.cloudinary.com/<cloud_name>/image/upload/v1/deer.jpg`
  * 縮放至 800px 寬且自動壓縮：`https://res.cloudinary.com/<cloud_name>/image/upload/w_800,c_scale,q_auto/v1/deer.jpg`
* 隱私控制：可在儀表板設定 Access Control 為 Restricted 或關閉公開目錄檢索。

---

## 4. 針對本專案的架構改造建議：Local Cache-First 模式

檢視專案中的 [`setting.json`](setting.json) 與 [`imgur.py`](imgur.py)，建議將圖片獲取機制標準化為「**本機快取優先（Cache-First）**」流程：

1. **在專案中建立快取目錄**（例如 `test_data/` 或 `.cache/`），並加入 [`.gitignore`](.gitignore)：
   ```gitignore
   test_data/
   .cache/
   ```
2. **重構下載輔助函式**：
   在執行任何 OpenCV 演算法前，由模組統一負責檢查檔案是否已存在本地：
   * **本地已存在**：直接回傳本地路徑（快速、離線可用）。
   * **本地不存在**：根據設定檔中指向的遠端 URL / 私有資源下載並寫入快取目錄。

### 推薦的 Helper 實作程式碼

```python
import os
import requests

CACHE_DIR = os.path.join(os.path.dirname(__file__), "test_data")
os.makedirs(CACHE_DIR, exist_ok=True)

def get_image(filename: str, remote_url: str, auth_token: str = None) -> str:
    """檢查本地快取，若無則自遠端下載"""
    local_path = os.path.join(CACHE_DIR, filename)
    if os.path.exists(local_path):
        return local_path

    print(f"[Cache-Miss] Downloading {filename} from {remote_url}...")
    headers = {"User-Agent": "Mozilla/5.0"}
    if auth_token:
        headers["Authorization"] = f"token {auth_token}"

    resp = requests.get(remote_url, headers=headers)
    resp.raise_for_status()

    with open(local_path, "wb") as f:
        f.write(resp.content)

    print(f"[Downloaded] Saved to {local_path}")
    return local_path
```

此架構能徹底解決換環境需要手動搬運圖片的問題，同時兼顧 Git 倉庫整潔與照片隱私。
