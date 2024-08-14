##### PRIVATE FUNCTION czzi934_input**(**p_cmd**)**

##### DEFINE p_cmd         **LIKE** type_t.chr1

##### 先做狀態判定   A insert R REPRODUCE U modify

  **IF** p_cmd **=** 'r' **THEN**
    **LET** l_cmd_t **=** 'r'
    **LET** p_cmd  **=** 'a'
  **ELSE**
    **LET** l_cmd_t **=** p_cmd
  **END** **IF**  

單頭段

#####  INPUT BY NAME g_pmwtuc_m.pmwtucdocno,g_pmwtuc_m.l_txt 

交互前

###### BEFORE INPUT

​         OPEN czzi934_cl USING g_enterprise,g_pmwtuc_m.pmwtucdocno 锁定表

​	     BEFORE FIELD l_txt  AFTER FIELD l_txt ON CHANGE l_txt ON ACTION controlp INFIELD l_txt 

完成INPUT交互后

######       AFTER INPUT

​     IF p_cmd <> 'u' THEN

​                inert 

​     ELSE

​                update

##### END INPUT



单身段

##### INPUT ARRAY g_pmwduc_d FROM s_detail1.*

##### BEFORE INPUT

###### 	CALL czzi934_b_fill() 这个是用单号去填充子单身 [ac]是行号

##### BEFORE ROW

###### 	OPEN czzi934_cl USING g_enterprise,g_pmwtuc_m.pmwtucdocno 锁定表

##### BEFORE INSERT  

​	在这个地方有写个自动添加项次

##### AFTER INSERT

​	CALL czzi934_insert_b('pmwduc_t',gs_keys,"'1'") 实际执行新增的脚本

##### BEFORE DELETE  

##### AFTER DELETE 这两个应该同 insert一样的逻辑

BEFORE FIELD pmwducseq   AFTER  CHANGE  ON ACTION controlp   

ON ACTION controlp INFIELD pmwduc000写个一个开窗的例子,

##### ON ROW CHANGE

###### END INPUT



##### DIALOG 

#####  BEFORE DIALOG 

##### ON ACTION accept

##### END DIALOG 



**END** **FUNCTION**