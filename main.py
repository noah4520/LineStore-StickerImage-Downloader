import os
from warnings import catch_warnings

# 爬蟲用套件
from bs4 import BeautifulSoup
import requests

# 系統用套件
import glob
from PIL import Image
import re

baseWidth = 512  # 初始化

input_ID = input("請輸入要下載的LineStore貼圖ID：")

response = requests.get(f"https://store.line.me/stickershop/product/{input_ID}/zh-Hant?ref=Desktop")
soup = BeautifulSoup(response.text, "lxml")

image_links = []  # 存放連結的迴圈

tempTitle = soup.find("p", {"class": "mdCMN38Item01Ttl"}).text  # 取得貼圖名稱

# 正則表達式轉換資料夾標題，防止建立資料夾錯誤
reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
tempTitle = re.sub(reg,'',tempTitle) 

# 切割字串，有待優化
for tempStr1 in soup.find_all("span", {"class": "mdCMN09Image FnPreview"}):
    tempStr2 = str(tempStr1).replace("<span class=\"mdCMN09Image FnPreview\" style=\"background-image:url(","")
    tempStr3 = str(tempStr2).replace(");\">","")
    imgLink = str(tempStr3).replace("</span>","")  # 無法將後面一次分割，只好分兩次...
    sliceLast = slice(-1)  # 切分最後的空白

    image_links.append(imgLink[sliceLast])  # 放入陣列

saveFile = tempTitle

if(len(image_links) > 0):
    
    print("\n圖片下載中，請稍後...\n")
    
    for index, link in enumerate(image_links):

        if not os.path.exists(saveFile):
            os.mkdir(saveFile)  # 建立資料夾

        img = requests.get(link)  # 下載圖片

        with open(f"{saveFile}\\" + input_ID + str(index+1) + ".png", "wb") as file:  # 開啟資料夾及命名圖片檔

            file.write(img.content)  # 寫入圖片的二進位碼

    imgs = glob.glob(f'./{saveFile}/*.png')  # 取得 demo 資料夾內所有的圖片

    print("\n圖片大小轉換中，請稍後...\n")

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

    input("\n下載完成，按下Enter後結束！")

else:
    input("\n輸入的ID發生錯誤，按下Enter後結束！")