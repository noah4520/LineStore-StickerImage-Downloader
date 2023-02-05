import os
from warnings import catch_warnings

# 爬蟲用套件
from bs4 import BeautifulSoup
import requests

# 系統用套件
import glob
from PIL import Image

# 正則表達式
import re

baseWidth = 512 # 初始化

input_ID = input("請輸入要下載的LineStore貼圖ID：")

response = requests.get(f"https://store.line.me/stickershop/product/{input_ID}/zh-Hant?ref=Desktop")
soup = BeautifulSoup(response.text, "lxml")

imageLinksAry = [] # 存放連結的迴圈

stickerType = "" # "static", "animation"

tempTitle = soup.find("p", {"class": "mdCMN38Item01Ttl"}).text  # 取得貼圖名稱

# 正則表達式轉換資料夾標題，防止建立資料夾錯誤
reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
tempTitle = re.sub(reg,'',tempTitle) 

# 切割字串
for tempStr0 in soup.find_all("li", {"class": "FnStickerPreviewItem"}):

    staticUrl = re.search(r'(?<=staticUrl" : ").*(?=", "fallbackStaticUrl" : ")', str(tempStr0)).group(0)
    animationUrl = re.search(r'(?<=animationUrl" : ").*(?=", "popupUrl" : ")', str(tempStr0)).group(0)

    # 狀態設定
    if(len(animationUrl)>1):
        imageLinksAry.append(animationUrl)
        stickerType = "animation"
    else:
        imageLinksAry.append(staticUrl)
        stickerType = "static"

saveFile = tempTitle

if(len(imageLinksAry) > 0):
    
    print("\n圖片下載中，請稍後...\n")
    
    for index, link in enumerate(imageLinksAry):

        if not os.path.exists(saveFile):
            os.mkdir(saveFile)  # 建立資料夾

        img = requests.get(link)  # 下載圖片

        with open(f"{saveFile}\\" + input_ID + str(index+1) + ".png", "wb") as file:  # 開啟資料夾及命名圖片檔

            file.write(img.content)  # 寫入圖片的二進位碼

    if(stickerType == "static"):

        imgs = glob.glob(f'./{saveFile}/*.png')  # 取得 demo 資料夾內所有的圖片
        
        print("\n靜態貼圖大小轉換中，請稍後...\n")

        for i in imgs:
            im = Image.open(i)

            wpercent = (baseWidth / float(im.size[0])) # 計算寬邊的比例
            hsize = int((float(im.size[1]) * float(wpercent))) # 計算長邊的應有比例

            size = im.size
            name = i.replace(f"./{tempTitle}\\","")
            im2 = im.resize((baseWidth,hsize), Image.Resampling.LANCZOS) # 調整圖片尺寸

            if not os.path.exists(f"{saveFile}"):
                os.mkdir(f"{saveFile}")  # 建立資料夾

            im2.save(f'./{saveFile}/{name}','png')   # 調整後存檔到 resize 資料夾

        input("\n靜態貼圖下載完成，按下Enter後結束！")
    
    elif(stickerType == "animation"):

        input("\n動態貼圖下載完成，按下Enter後結束！")

else:
    input("\n輸入的ID發生錯誤，按下Enter後結束！")