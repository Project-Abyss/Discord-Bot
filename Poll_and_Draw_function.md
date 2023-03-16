# Command Mode
## Draw Lottery

* 頻道內的成員資訊：`!MembersInfo` or `!info`

```
    說明：查看頻道內成員的姓名與人數（不包括機器人）。
    【 範例：!info 】
```

* 依據指定成員或身份組抽籤

```
    說明：選擇多個指定成員或身份組後，再抽簽！
    【 範例：!mix [欲抽人數] @身份組1 @成員1 @成員2 @身份組2 @身份組3 @成員3 】
    【 範例：!mix 2 @RD @bessyhuang @PM 】
```

*  依據指定成員抽籤         

```
    說明：被點到的人都逃不掉！
    【 範例：!member [欲抽人數] @成員1 @成員2 @成員3 】
    【 範例：!member 1 @Nima @bessyhuang @紙只 】
```

*  依據身份組抽籤           

```
    說明：選擇多個身份組後，再抽簽！
    【 範例：!role [欲抽人數] @身份組1 @身份組2 @身份組3 】
    【 範例：!role 1 @RD 】
```

---
# User Interface Mode
## Draw Lottery
```
!menu
```

![image](https://user-images.githubusercontent.com/42068007/225383582-0d1ffb8d-c80b-4497-a227-1c965fdcc716.png)
![image](https://user-images.githubusercontent.com/42068007/225383719-ba45cd12-5887-4022-aba4-d7bd5a75326b.png)
![image](https://user-images.githubusercontent.com/42068007/225383985-9f064448-992e-4615-a708-bea9ac3d9da7.png)
![image](https://user-images.githubusercontent.com/42068007/225384136-6659fa18-dfb9-4925-9101-af1432db85c8.png)

---
# 投票
此功能提供使用者針對不同議題進行投票表決，並分為**單票制**和**多票制**兩種投票制度，以下詳述之。
## 單票制指令
```
!SingleAnswer (投票標題) (投票截止日期) (投票截止時辰) (選項)
```
* 投票結果會呈現在該投票介面當中

## 多票制指令
```
!MutiAnswer (投票標題) (投票截止日期) (投票截止時辰) (選項)
```
* 投票結果會輸出成排行榜，並且以最高票依序列出

若是無法準確記住參數的排序，這邊也提供了語法產生介面，
可以藉由 `!menu` 指令呼叫，並選擇 `Make a Poll` 選項，
依照介面所提供的問題填寫，便能取得單票制或多票制的指令語法。
