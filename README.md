# LineStore-StickerImage-Downloader

下載LineStore的貼圖圖片，並轉為Telegram貼圖可使用的格式。

## 功能
Telegram預設貼圖一邊**至少為512px**，且另一邊**不可超過512px**。

此工具會批次將圖片寬度設定成512px，並自動縮放圖片高度。
下載後的圖片資料夾會儲存在執行路徑下。

## 如何使用
1. 輸入*LineStore*貼圖頁面上的網址ID。
2. 等待完成～


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