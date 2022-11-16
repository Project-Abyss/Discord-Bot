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

### 建立虛擬環境並安裝套件
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
  * 透過 requirements.txt 安裝所需套件
  ```
  pip install -r requirements.txt
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
### 創建機器人
若須了解如何使用 Discord Developer Portal 創建機器人，可參考[文件](https://github.com/Project-Abyss/Discord-Bot/blob/main/create_discord_bot_application.md)。
### 啟動機器人
開啟虛擬環境後，在當前路徑執行 ```python main.py```，即可開啟機器人。
### 使用指令
在機器人有權限訪問的文字頻道中輸入指令即可
* 更改**功能訊息**自動刪除時間
  * 預設時間為 60 秒
```
>time <秒數>
```
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
