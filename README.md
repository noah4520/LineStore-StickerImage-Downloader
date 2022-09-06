# LineStore-StickerImage-Downloader
下載LineStore的圖片，並轉為Telegram貼圖可上傳的格式。

## 功能
1. 透過輸入LineStore貼圖頁面的網址ID，下載該貼圖.png圖片檔。
2. 轉換成寬度為512px的.png圖片檔，高度等比例縮放。

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