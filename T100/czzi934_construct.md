### PRIVATE FUNCTION czzi934_construct()

 DEFINE ls_wc       STRING 

##### 1318:DIALOG ATTRIBUTES(UNBUFFERED,FIELD ORDER FORM)

##### 		1单头

###### 		1321:CONSTRUCT BY NAME g_wc ON pmwtucdocno,l_txt,pmwtucownid,pmwtucowndp,pmwtuccrtid,pmwtuccrtdp,pmwtuccrtdt, 

​					BEFORE CONSTRUCT

​					AFTER FIELD pmwtuccrtdt

​					AFTER FIELD pmwtuccnfdt

​					BEFORE FIELD pmwtucdocno

​					AFTER FIELD pmwtucdocno

​					ON ACTION controlp INFIELD pmwtucdocno

​				

```
g_wc = "pmwtucdocno='21212' and pmwtucownid='121' and pmwtucowndp='212' and pmwtuccrtid='212'"
```



###### 		1649:END CONSTRUCT

##### 		2单身 且只对第一行收集

###### 		1652E:CONSTRUCT g_wc2_table1 ON pmwducseq,pmwduc000,pmwduc011,pmwduc001,pmwduc002,pmwduc003,pmwduc007

​					BEFORE CONSTRUCT

​					BEFORE FIELD pmwducseq

​					AFTER FIELD pmwducseq

​					ON ACTION controlp INFIELD pmwducseq

​					--g_wc2 = "pmwduc001='7878' and pmwduc007='8787878'"

###### 		1920:END CONSTRUCT

##### 1969:END DIALOG

BEFORE DIALOG

ON ACTION qbe_select

ON ACTION qbe_save

ON ACTION accept

​		ACCEPT DIALOG 

ON ACTION cancel
         EXIT DIALOG 

### END FUNCTION

执行流程为:

```python
main->OPTIONS->初始化CALL cl_ap_init("czz","")->锁定表LET g_forupd_sql->准备单头信息g_sql->OPEN WINDOW 
->UI初始化CALL cl_ui_init()->程序初始CALL czzi934_init()->进入交互CALL czzi934_ui_dialog()->ON ACTION query
-> czzi934_construct()->采列表的数据czzi934_browser_fill 收集到g_browser->抓取单头信息czzi934_fetch(这里会有重读EXECUTE czzi934_master_referesh)(show)->最终到CALL g_curr_diag.setCurrentRow("s_detail1",1)
```

