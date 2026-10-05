# 待辦事項 (TODO)

本文件記錄本專案（OpenCV Python Snippets）測試用圖檔之盤點清單、替換規劃與後續重構任務。

---

## 1. 測試圖檔需求盤點清單 (Asset Inventory)

### A. 原 Imgur 遠端圖檔（需改由本地或 Release 提供）
- [ ] **`deer.png`**：用於 [`imgur.py`](imgur.py)、[`loadimgur.py`](loadimgur.py)（測試圖片下載與顯示）
- [ ] **`lego.jpg`**：用於 [`loadimgur.py`](loadimgur.py)（預設展示圖片）
- [ ] **`lena.jpg` / `lena.png`**：用於 [`imende.py`](imende.py)、[`loadimgur.py`](loadimgur.py)、[`split.py`](split.py)（經典影像編解碼與通道處理）
- [ ] **`vwcar.jpg`**：用於 [`imgur.py`](imgur.py)（汽車展示候選圖）
- [ ] **`smallhorse.jpg`**：用於 [`imgur.py`](imgur.py)（小馬展示候選圖）

### B. 原本設定於 `setting.json` 的本機圖檔（原預期路徑 `~/Pictures/data`）
- [ ] **`flower_and_bee.jpg`**：用於 [`add_border.py`](add_border.py)（邊框擴增測試圖）
- [ ] **`47916-wallpaper.jpg`**：用於 [`split.py`](split.py)（RGB 通道分離與平均值預處理）
- [ ] **`img2668.jpg`**：用於 [`readim.py`](readim.py)（批次連續讀圖與畫線）
- [ ] **`img2980.jpg`**：用於 [`readim.py`](readim.py)（批次連續讀圖與畫線）
- [ ] **`eefb19f7599a5.jpg`**：用於 [`readim.py`](readim.py)（批次連續讀圖與畫線）

### C. 各獨立演算法腳本寫死之單元測試圖
- [ ] **`top.jpg`**, **`bot.jpg`**：用於 [`cvadd.py`](cvadd.py)（上下與左右影像拼接）
- [ ] **`img1.jpg`**, **`img2.jpg`**：用於 [`cvutil.py`](cvutil.py)（影像水平組合與重設大小）
- [ ] **`c50.jpg`**：用於 [`persp-transform/go.sh`](persp-transform/go.sh)（四點透視變換範例，如卡片/紙張/名片）
- [ ] **`headPose.jpg`**：用於 [`headPose.py`](headPose.py)（3D 人臉姿態估計，需包含特定座標之人臉特徵）
- [ ] **`./data/*.jpg`**：用於 [`faceland.py`](faceland.py)（Dlib 68 點人臉特徵檢測，需人臉照片與 `shape_predictor_68_face_landmarks.dat`）

---

## 2. 自有圖檔替換與準備規劃 (Asset Preparation)

- [ ] **挑選並拍攝/裁切自有照片 (約 5~8 張)**：
  - **一般靜物/風景照**：可通吃大部分演算法測試（替換 `flower_and_bee`、`wallpaper`、`img*`、`top/bot`、`img1/2` 等）。
  - **透視變換用照**：拍攝一張放在平面上的長方形物體（書籍、卡片或名片，替換 `c50.jpg`）。
  - **人臉照片 (選用)**：若未來需執行 `headPose.py` 或 `faceland.py` 需準備人臉清晰的正面照。
- [ ] **尺寸與體積優化**：
  - 適度縮小長寬（建議 1080p 或 2K 即可），單圖控制在 1MB ~ 3MB 以內。
- [ ] **打包為 Release 壓縮檔**：
  - 將上述圖檔統一歸檔為 `test_images.tar.gz`。
  - 上傳至獨立的私有倉庫 Release 或目前的倉庫 Release。

---

## 3. 程式碼與架構重構任務 (Code Refactoring)

- [ ] **修正 `setting.json` 寫死絕對路徑問題**：
  - 將 `"/home/user/Pictures/data"` 改為相對於專案根目錄的 `"./data"`。
- [ ] **將圖檔快取目錄加入 `.gitignore`**：
  - 在 `.gitignore` 中加入 `data/` 與 `test_data/`，避免圖檔被意外 commit 進 Git。
- [ ] **新增安裝與同步腳本 (`setup_assets.py`)**：
  - 於環境建置/安裝階段執行，一次性自動由 Release 下載並解壓縮至 `./data/`。
- [ ] **重構 `imgur.py` 與 `loadimgur.py`**：
  - 移除對 Imgur 外部網路的即時依賴，改為讀取本地快取目錄。
