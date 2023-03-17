# Discord-Bot
## Background (專案概述)
根據提供的七個公告範本及抽籤投票功能，製作出一可套用特定模板並發送公告或是進行投票抽籤的 Discord 機器人。

主要使用 Python 的 discord.py 套件撰寫機器人的指令，包括：
* 呼叫機器人
* 規範模板格式
* 將使用者輸入的內容套用於模板
* 發布公告
* 抽籤
* 投票

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
└───function
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
!time <秒數>
```
* 呼叫選單
```
!menu
```
> 共包含 7 種公告模板及 2 個小工具
> * **模板：**
>    1. Meeting Announcement 1
>    2. Meeting Announcement 2
>    3. Announcement
>    4. 對外課程公告
>    5. 對內課程公告
>    6. 遺忘書目
>    7. FaceBook 貼文發表
> * **小工具：**
>    1. Draw Member & Role
>    2. Make a Poll
* 關閉機器人
```
!quit
```
---
## 抽籤
針對抽籤小工具，本團隊提供「 User Interface 」與「 Command 」兩種模式，提供予使用者選擇。
* 「 User Interface 模式 」合併了**指定成員**和**身份組**兩種抽籤方式，並且藉由圖形化介面提供使用者輸入提示。
* 「 Command 模式 」除了允許使用者**查詢頻道內的成員資訊**，還能夠依據**指定成員**、**身份組**以及**指定成員或身份組**三種指令模式進行抽籤，以下詳述之。
### Command
#### 頻道內的成員資訊
```
    說明：查看頻道內成員的姓名與人數（不包括機器人）。
    【 範例：!info 】
    【 範例：!MembersInfo 】
```

#### 依據指定成員抽籤
```
    說明：被點到的人都逃不掉！
    【 範例：!member [欲抽人數] @成員1 @成員2 @成員3 】
    【 範例：!member 1 @Nima @bessyhuang @紙只 】
```

#### 依據身份組抽籤           
```
    說明：選擇多個身份組後，再抽簽！
    【 範例：!role [欲抽人數] @身份組1 @身份組2 @身份組3 】
    【 範例：!role 1 @RD 】
```

#### 依據指定成員或身份組抽籤
```
    說明：選擇多個指定成員或身份組後，再抽簽！
    【 範例：!mix [欲抽人數] @身份組1 @成員1 @成員2 @身份組2 @身份組3 @成員3 】
    【 範例：!mix 2 @RD @bessyhuang @PM 】
```
### User Interface

## 投票
### Command
此功能提供使用者針對不同議題進行投票表決，並分為**單票制**和**多票制**兩種投票制度，以下詳述之。
#### 單票制指令
```
!SingleAnswer (投票標題) (投票截止日期) (投票截止時辰) (選項)
```
* 投票結果會呈現在該投票介面當中

#### 多票制指令
```
!MutiAnswer (投票標題) (投票截止日期) (投票截止時辰) (選項)
```
* 投票結果會輸出成排行榜，並且以最高票依序列出

### User Interface
若是無法準確記住參數的排序，這邊也提供了語法產生介面，
可以藉由 `!menu` 指令呼叫，並選擇 `Make a Poll` 選項，
依照介面所提供的問題填寫，便能取得單票制或多票制的指令語法。

---

## Contributing (專案貢獻)
### Contributors
[許雅喬 Ya-Chiao Hsu](https://github.com/Chiao52)@Abyss-TeamB (Project Manager/Maintainer)

[宋安琪 An-Chi Sung](https://github.com/Anzheim)@Abyss-TeamB (Author/Maintainer)

[王筱鈞 Hsiao-Chun Wang](https://github.com/momo8042)@Abyss-TeamB (Author/Maintainer)

[黃子軒 Tzu-Hsuan Huang](https://github.com/Nima-Huang)@Abyss-TeamA (Project Manager/Maintainer)

[黃丰嘉 Feng-Chia Huang](https://github.com/bessyhuang)@Abyss-TeamA (Author/Maintainer)

[許至齊 Zhi-Qi Xu](https://github.com/xkeBANg)@Abyss-TeamA (Author/Maintainer)

