import os
from warnings import catch_warnings

# 爬蟲用套件
from bs4 import BeautifulSoup
import requests

# 系統用套件
import glob
from PIL import Image
import shutil

baseWidth = 0  # 初始化

input_ID = input("請輸入要下載的LineStore貼圖ID：")
needChangeSizeInput = input("是否需要調整圖片大小(Y/N)：")

if(needChangeSizeInput == "Y" or needChangeSizeInput == "y"):
    isNeedChangeSize = False

    while isNeedChangeSize == False:
        try:
            baseWidth = int(input("請輸入寬度(px)："))
            isNeedChangeSize = True
        except:
            print("\n輸入寬度有錯，請重新輸入一次\n")
            isNeedChangeSize = False
else:
    isNeedChangeSize = False

response = requests.get(f"https://store.line.me/stickershop/product/{input_ID}/zh-Hant?ref=Desktop")
soup = BeautifulSoup(response.text, "lxml")

image_links = []  # 存放連結的迴圈

tempTitle = soup.find("p", {"class": "mdCMN38Item01Ttl"}).text  # 取得貼圖名稱

# 切割字串，有待優化
for tempStr1 in soup.find_all("span", {"class": "mdCMN09Image FnPreview"}):
    tempStr2 = str(tempStr1).replace("<span class=\"mdCMN09Image FnPreview\" style=\"background-image:url(","")
    tempStr3 = str(tempStr2).replace(");\">","")
    imgLink = str(tempStr3).replace("</span>","")  # 無法將後面一次分割，只好分兩次...
    sliceLast = slice(-1)  # 切分最後的空白

    image_links.append(imgLink[sliceLast])  # 放入陣列

if(isNeedChangeSize == True):
    saveFile = "Temp"
    resizeFile = tempTitle
else :
    saveFile = tempTitle

if(len(image_links) > 0):
    
    print("\n圖片下載中，請稍後...\n")
    
    for index, link in enumerate(image_links):

        if not os.path.exists(saveFile):
            os.mkdir(saveFile)  # 建立資料夾

        img = requests.get(link)  # 下載圖片

        with open(f"{saveFile}\\" + input_ID + str(index+1) + ".png", "wb") as file:  # 開啟資料夾及命名圖片檔

            file.write(img.content)  # 寫入圖片的二進位碼

    if(isNeedChangeSize == True):

        imgs = glob.glob(f'./{saveFile}/*.png')  # 取得 demo 資料夾內所有的圖片

        print("\n圖片大小轉換中，請稍後...\n")

        for i in imgs:
            im = Image.open(i)

            wpercent = (baseWidth / float(im.size[0])) # 計算寬邊的比例
            hsize = int((float(im.size[1]) * float(wpercent))) # 計算長邊的應有比例

            size = im.size
            name = i.replace(f"./{saveFile}\\","")
            im2 = im.resize((baseWidth,hsize), Image.Resampling.LANCZOS) # 調整圖片尺寸

            if not os.path.exists(f"{resizeFile}"):
                os.mkdir(f"{resizeFile}")  # 建立資料夾

            im2.save(f'./{resizeFile}/{name}','png')   # 調整後存檔到 resize 資料夾
            os.remove(i)

        shutil.rmtree(f"./{saveFile}") # 強制刪除

    input("\n下載完成，按下Enter後結束！")

else:
    input("\n輸入的ID發生錯誤，按下Enter後結束！")