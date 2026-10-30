# 測試圖檔託管與跨平台同步方案建議

本文件針對此專案的圖檔管理需求（主倉庫輕量化、照片私密不公開、跨平台/跨機器自動同步）進行架構分析與方案建議。

---

## 1. 核心需求與背景限制

1. **避免 Git 倉庫膨脹**：測試用圖檔不直接 commit 進目前的 `opencv_python` 程式碼倉庫，保持 Git Clone 與更新時的輕巧快速。
2. **私密性與自有圖片**：使用自己拍攝的風景/靜物照片（無版權風險、可自由裁切調整解析度），**不希望被公開索引或被大眾隨意瀏覽**。
3. **跨平台多環境自動拉取**：在不同作業系統與開發環境中，不需要每次手動傳輸圖檔；腳本執行時自動從遠端同步下載至本地。
4. **圖片來源可控**：測試素材透過私有 GitHub Release 發佈，再下載到本機使用；程式執行時不從外部圖片 URL 讀取素材。

---

## 2. 方案比較與評估

| 方案 | 隱私性與安全性 | 免費額度 / 成本 | 跨平台設定複雜度 | 適合場景 |
| :--- | :--- | :--- | :--- | :--- |
| **方案 A：獨立私有 GitHub 倉庫 (推薦)** | **高** (Private 權限控管) | 免費 (一般個人帳號均支援) | **低** (開發環境通常已具備 GitHub Token / SSH) | 既有 GitHub 開發者、希望完全私密且零額外服務成本 |
| **方案 B：Cloudflare R2 物件儲存** | **中 ~ 高** (可選 S3 金鑰或未列出長路徑) | 10 GB 儲存免費，**完全免流量費** | **中** (需 Cloudflare 帳號，可免金鑰或使用 `boto3`) | 適合需要直接存取且希望自主控管的情境 |
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

* **模式 1：Unlisted (未列出/隱密路徑)**
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

## 4. 本專案的圖片素材流程

測試圖片由私有 GitHub Release 提供，使用 [`fetch_assets.sh`](fetch_assets.sh) 下載並解壓縮至 `./data/`。也可以透過 `./fetch_assets.sh -i <archive.zip>` 使用本機提供的壓縮檔。OpenCV 範例從本機設定路徑讀取圖片，不在程式執行期間連線下載圖片。
