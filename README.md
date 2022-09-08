# LineStore-StickerImage-Downloader

下載LineStore的圖片，並轉為Telegram貼圖可上傳的格式。

Telegram預設貼圖一邊**至少為512px**，且另一邊**不可超過512px**。
目前為了支援功能泛用性，可自行輸入。

## 功能
1. 透過輸入*LineStore*貼圖頁面的網址ID，下載該貼圖.png圖片檔。
2. 可根據輸入值轉調整下載的圖片檔寬度，圖片高度將等比例縮放。

## 安裝
clone專案之後，執行安裝所需的套件：

```
pip install requests
```
```
pip install beautifulsoup4
```
```
pip install lxml
```
```
pip install Pillow
```

## 我想直接使用
為了使用方便，已透過pyinstaller包裝成exe檔，可直接開啟使用

```
StickerImageDownloader.exe
```