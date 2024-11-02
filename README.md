# Python 初始化設定
以下是先從打開 VS 到建立 Python Notebook 的過程
1. 打開 VS
2. 開啟新檔案 (Ctrl + Alt + N)
3. 點選 Python
4. 創造專案資料夾
5. 創造 Python script (在左邊的專案欄位當中，右鍵 --> New File --> [檔名].py)
6. 然後在上面要輸入要載入的 Python 環境，這樣就算完成了!

# Git 初始化設定
1. 打開 VS
2. 然後要要在右下角創造新的 terminal 出來，才可以呼叫 git，不然都會困在Python Kernal 中
3. 要先設定基本資料
    git config --global user.name "JPChen"
    git config --global user.email "wind113@hotmail.com"
    git init

# 更新相關設定
    git add .
    git commit -m "[上傳資訊]"
    git log : 可以看到完整的紀錄
    git log --oneline : 可以看到簡短的紀錄 (主要是在看序號和註解，所以應該也夠用惹)

# 上傳至 Github 
1. 打開 Github 
2. 左上角選單中選擇 Home ---> 綠色的 New ---> 輸入專案名稱 ---> Enter
3. 下方有範例 Code 可以回到 VS 裡面 Git Terminal 複製貼上就好
4. (記得上傳前要先更新 Git 再上傳!)
5. git push : 將寫好的東西上傳到 Github 上面