```
main->OPTIONS->初始化CALL cl_ap_init("czz","")->锁定表LET g_forupd_sql->准备单头信息g_sql->OPEN WINDOW 
->UI初始化CALL cl_ui_init()->程序初始CALL czzi934_init()->进入交互CALL czzi934_ui_dialog()->ON ACTION modify
b:czzi934_modify
->事务开始CALL s_transaction_begin
->锁表OPEN czzi934_cl USING g_enterprise,g_pmwtuc_m.pmwtucdocno
->刷新EXECUTE czzi934_master_referesh USING g_pmwtuc_m.pmwtucdocno INTO g_pmwtuc_m.pmwtucdocno,g_pmwtuc_m.pmwtucownid
	刷新一般后跟show()
e:CALL czzi934_input("u")
B:czzi934_input(U) U 是update
->
```

