## 設定相關紀錄

1. pyinstaller包裝方法（含icon）

  ```pyinstaller -F main.py -i "\resource\Icon.ico"```

  若失敗則將icon移動至根目錄下

  ```pyinstaller -F main.py -i Icon.ico```