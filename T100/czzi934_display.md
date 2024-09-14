 **display** "aaaaaaaaaaaaaa" **to** pmwtucdocno  明确这个pmwtucdocno就是栏位了

另一种写法是 **DISPLAY** **BY** **NAME** g_pmwtuc_m.pmwtucdocno

我估计这两个地方不同的写法,类似vue的自动解包的原理

```vue
let queryinput = ref('')  在模板中queryinput不用写.value
```

### czzi934_show()  主要的代码显示单头的信息.

```sql
先填充单身:
IF g_bfill = "Y" THEN
      CALL czzi934_b_fill() #單身填充
      CALL czzi934_b_fill2('0') #單身填充
   END IF
#將資料輸出到畫面上
   DISPLAY BY NAME g_pmwtuc_m.pmwtucdocno,g_pmwtuc_m.l_txt,g_pmwtuc_m.pmwtucownid,g_pmwtuc_m.pmwtucownid_desc, 
       g_pmwtuc_m.pmwtucowndp,g_pmwtuc_m.pmwtucowndp_desc,g_pmwtuc_m.pmwtuccrtid,g_pmwtuc_m.pmwtuccrtid_desc, 
       g_pmwtuc_m.pmwtuccrtdp,g_pmwtuc_m.pmwtuccrtdp_desc,g_pmwtuc_m.pmwtuccrtdt,g_pmwtuc_m.pmwtucmodid, 
       g_pmwtuc_m.pmwtucmodid_desc,g_pmwtuc_m.pmwtucmoddt,g_pmwtuc_m.pmwtuccnfid,g_pmwtuc_m.pmwtuccnfid_desc, 
       g_pmwtuc_m.pmwtuccnfdt
```

单身

```
  DISPLAY BY NAME g_pmwduc_d[l_ac].pmwducseq,g_pmwduc_d[l_ac].pmwduc009,g_pmwduc_d[l_ac].pmwduc010
  g_pmwduc_d是个二维数组,类似cells(行,列),其中行固定为数字从1开始,列为字段的名字.
```

最终的显示在这个地方



```sql
DISPLAY ARRAY g_pmwduc_d TO s_detail1.* ATTRIBUTES(COUNT=g_rec_b) #page1  
    
            BEFORE ROW
               #顯示單身筆數
               CALL czzi934_idx_chk()
               #確定當下選擇的筆數
               LET l_ac = DIALOG.getCurrentRow("s_detail1")
               LET g_detail_idx = l_ac
               LET g_detail_idx_list[1] = l_ac
               CALL g_idx_group.addAttribute("'1',",l_ac)
               
               #add-point:page1, before row動作 name="ui_dialog.page1.before_row"

               #end add-point
               
            BEFORE DISPLAY
               #如果一直都在單身1則控制筆數位置
               IF g_loc = 'm' THEN
                  CALL FGL_SET_ARR_CURR(g_idx_group.getValue("'1',"))
               END IF
               LET g_loc = 'm'
               LET l_ac = DIALOG.getCurrentRow("s_detail1")
               LET g_current_page = 1
               #顯示單身筆數
               display "aaaaaaaaaaaaaa" to pmwtucdocno
               CALL czzi934_idx_chk()
               #add-point:page1自定義行為 name="ui_dialog.page1.before_display"

               #end add-point
               
            #自訂ACTION(detail_show,page_1)
            
               
            #add-point:page1自定義行為 name="ui_dialog.page1.action"

            #end add-point
               
         END DISPLAY
```

附一些总结图片

![image-20240820111730126](https://gitee.com/aiiw/images/raw/master/img/image-20240820111730126.png)

###  \#CALL g_curr_diag.setCurrentRow("s_detail1",1)

```
g_curr_diag 这是一个数据表控件,setCurrentRow设置当前行,s_detail1这个就是数据表
```

