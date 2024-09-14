2609:PRIVATE FUNCTION czzi934_input(p_cmd)

​	DEFINE  p_cmd                 LIKE type_t.chr1

​	先做狀態判定 r和a 是insert u 是 update

##### 	2718:DIALOG ATTRIBUTES(UNBUFFERED,FIELD ORDER FORM)

---------

​			2722:#單頭段

​			INPUT BY NAME g_pmwtuc_m.pmwtucdocno,g_pmwtuc_m.l_txt 

​					BEFORE INPUT

​					BEFORE FIELD pmwtucdocno

​					AFTER FIELD pmwtucdocno 栏位开窗

​					..........有一个判断p_cmd  是否=U 不是,直接insert 是 直接update 

​			END INPUT

-------------------

​				2961:#单身

​				INPUT ARRAY g_pmwduc_d FROM s_detail1.*

​							BEFORE INPUT (这里主要做b_fill 填充单身)

##### 							BEFORE ROW

​							    OPEN czzi934_cl USING g_enterprise,g_pmwtuc_m.pmwtucdocno 

​							     (2676:czzi934_cl :  是 select * from 单身 where 单据=G.单据号  =>形成一张二维表.注意这里的czzi934_cl已经重新定义,取的是单身

​							    外部全局czzi934_cl是锁定单头.)

​							    FETCH czzi934_bcl INTO g_pmwduc_d[l_ac].pmwducseq

​								这个地方复杂 大概的意思就是编辑,应该是不会区分p_cmd是新增还是修改,因为这个表格的改动都是编辑的.

​									3701	            IF g_rec_b >= l_ac   g_rec_b 是取b_fill 填充后的单身数组的长度与l_ac   (取ARR_CURR() 获取 当前行)对比

​															如果是单身数组>当前点击的行,就是定位到已经有的数据,这就走update流程,获取走的是新增流程.

​								**BEFORE** **INSERT** 

​											这个有数据新增时,会提前准备,例如写过一个自动添加项次的.

​								AFTER INSTER

​											这个会判断有没有重复,如果没有,就调用 CALL cqct098_insert_b('qckduc_t',gs_keys,"'1'")进行新增

​								**ON** **ROW** **CHANGE**

​											这个只在当前行更改后,直接有更新的脚本.



​								after row

​												提交

​								after input

​												空的

​				END INPUT

--------------------

​				3731:其他

​				{<section id="czzi934.input.other" type="s" >}

​				BEFORE DIALOG 注意后续只有一个END DIALOG 所以不知道这个是不是没有END DIALOG

##### 	3829:END DIALOG

3835:END FUNCTION

附:单身的场景

| 场景       | 执行情况                                                     |
| ---------- | ------------------------------------------------------------ |
| 进入表格   | BEFORE INPUT BEFORE ROW BEFORE FIELD                         |
| 同列移动   | [ON CHANGE] (for field A, if value has changed)                           AFTER FIELD (for field A)                        BEFORE FIELD (for field B) |
| 不同列移动 | AFTER FIELD (for field A in the current row)                                                                                                                                                                      [AFTER INSERT] (if a new row was inserted or new row was appended and modified)                                                                                                  [ON ROW CHANGE] (if values have changed in current row)                                                                                                                                           AFTER ROW (for the current) BEFORE ROW (the new row) BEFORE FIELD (for field B in the new row) |
| 按下確定   | [ON CHANGE] AFTER FIELD [AFTER INSERT] (if a new row was created) [ON ROW CHANGE] (if values have changed) AFTER ROW AFTER INPUT |
| 按下取消   | AFTER ROW       AFTER INPUT                                  |

附流程:

```
main->OPTIONS->初始化CALL cl_ap_init("czz","")->锁定表LET g_forupd_sql->准备单头信息g_sql->OPEN WINDOW 
->UI初始化CALL cl_ui_init()->程序初始CALL czzi934_init()->进入交互CALL czzi934_ui_dialog()->ON ACTION inert
-> CALL cqct098_input("a")->单头判断是更新还是新增->单身
```

附单身图:

![image-20240815175606242](https://gitee.com/aiiw/images/raw/master/img/image-20240815175606242.png)