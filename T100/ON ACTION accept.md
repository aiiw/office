```
ON ACTION accept
         ACCEPT DIALOG
 
ON ACTION cancel
         LET INT_FLAG = 1
         EXIT DIALOG       
```

### 这两个只存在input construct 的对话框,我理解是一个是同意,一个是取消,两者都是结束这个对话框,不然这个对话框一直都是在交互.

其中ACCEPT DIALOG后,还有对 after field执行代码,而EXIT DIALOG是直接退出,执行下一个代码