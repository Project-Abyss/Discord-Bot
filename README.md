# Discord-Bot
## Background (專案概述)
根據甲方所提供的七個公告範本，製作出一可套用特定模板並發送公告的 Discord 公告機器人。

主要使用 Python 的 discord.py 套件撰寫機器人的指令，包括：
* 呼叫機器人
* 規範模板格式
* 將使用者輸入的內容套用於模板
* 發布公告

## Installation (如何安裝)
### 要求環境
* Python == 3.10.4

### 透過 Discord Developer Portal 創建機器人
* 網址：https://discord.com/login?redirect_to=%2Fdevelopers
#### 登入 Discord 帳號後點選左上角的 **Applications**

![image](https://user-images.githubusercontent.com/88641414/201662563-682eeb32-a6d5-419f-a6f7-57744020d96b.png)

* 選擇右上角的 **New Application** 建立機器人
* 輸入機器人的名字 (同時會變成機器人進伺服器時預設的身分組名稱)

![image](https://user-images.githubusercontent.com/88641414/201662930-7df668c8-08e3-4af2-9806-a36b4c43f24c.png)
#### 點選 **SETTING - BOT**

![image](https://user-images.githubusercontent.com/88641414/201663823-5121c64c-6a74-498e-ab07-b4119f1d5de2.png)
* 將 **Privileged Gateway Intents** 以下的選項全部設定啟用

![image](https://user-images.githubusercontent.com/88641414/201664328-bcca9b3c-00b7-4f00-9144-33036398ab87.png)
* 上滑到 **Build-A-Bot** 點選 **Reset TOKEN** 以取得機器人的 TOKEN

![image](https://user-images.githubusercontent.com/88641414/201665777-59691ac6-88e0-41f3-9f7a-c06d43f8d712.png)
* 將其複製後儲存於 ```.env``` 檔案中的 **TOKEN**
#### 點選 **OAuth2** 底下的 **URL Generator**

![image](https://user-images.githubusercontent.com/88641414/201666343-cba37332-4688-4b44-ac64-43e8db5f70a4.png)
* 在 **Scope** 中勾選 **BOT**

![image](https://user-images.githubusercontent.com/88641414/201666938-f3fe77cb-7d0c-4b69-85f9-4835df5db329.png)
* 在 **BOT PERMISSIONS** 中勾選以下允許權限，主要根據以下功能：
  * 管理、傳送、讀取訊息及討論串
  * 允許提及伺服器內部成員
  
![image](https://user-images.githubusercontent.com/88641414/201670230-1c1659db-ccff-4715-b18c-3c2065bb2757.png)
 * 複製 **GENERATED URL** 產生的網址，到瀏覽器執行後，即可將機器人引入自己具有**管理權**的伺服器

### 建立虛擬環境
* 建立一資料夾，存放虛擬環境以及下載的 Discord Bot 相關檔案
  * 安裝 virtualenv
  ```
  pip install virtualenv
  ```
  * 創建虛擬環境
  ```
  virtualenv <虛擬環境名稱>
  # or
  python -m venv <虛擬環境名稱>
  ```
  * 在當前路徑執行 virtualenv
  ```
  <虛擬環境名稱>\Scripts\activate
  ```
* 當前路徑如下所示：
```
<資料夾名稱>
│   <虛擬環境名稱>
|   main.py
|   README.md
|   requirements.txt
|   .env
|   
└───cogs
│   │   menu.py
│   │   ...
│   
```
## Usage (如何使用)
### 啟動機器人
開啟虛擬環境後，在當前路徑執行 ```python main.py```，即可開啟機器人。
### 使用指令
在機器人有權限訪問的文字頻道中輸入指令即可
* 呼叫選單
```
>menu
```
* 關閉機器人
```
>quit
```

## Contributing (專案貢獻)
### Contributors
[許雅喬 Ya-Chiao Hsu](https://github.com/Chiao52)@Abyss-TeamB (Project Manager/Maintainer)

[宋安琪 An-Chi Sung](https://github.com/Anzheim)@Abyss-TeamB (Author/Maintainer)

[王筱鈞 Hsiao-Chun Wang](https://github.com/momo8042)@Abyss-TeamB (Author/Maintainer)
