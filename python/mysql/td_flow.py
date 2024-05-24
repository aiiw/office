import arrow

import connector

mydb = connector.connect(
    host="192.168.0.101",
    user="root",
    port="3336",
    passwd="myoa888",
    database="TD_OA",
    auth_plugin='mysql_native_password',  # 要加上这个东东才行,

)
mycursor = mydb.cursor()
mycursor.execute("select max(run_id) from `flow_run`")
result = mycursor.fetchone()
RUN_ID = result[0] + 1
print(RUN_ID)
RUN_NAME="ERP财务权限申请表202111180010"#标题
BEGIN_USER="960";#发起人
BEGIN_DEPT='235'#部门
BEGIN_TIME=arrow.now().format('YYYY-MM-DD HH:mm:ss')
FLOW_ID="254"
DEL_FLAG="0" #删除标记(0-未删除,1-已删除)删除后流程实例可在工作销毁中确实删除或还原
PARENT_RUN="0" #父流程ID 默认为0
ARCHIVE="0" #是否归档(0-否,1-是)
work_level="0" #工作等级 0-普通 1-重要 2-紧急
value=('null',RUN_ID, RUN_NAME, FLOW_ID, BEGIN_USER,BEGIN_DEPT, BEGIN_TIME,'null', '', '', DEL_FLAG, '', PARENT_RUN, '', '', '', '', ARCHIVE, '', work_level,'')
sql1=f"INSERT INTO flow_run_test01  VALUES {value}"
mycursor.execute(sql1)
mydb.commit()
################################################################
flow_auto_num='1'
sql2='INSERT INTO flow_data_11 (run_id,run_name,begin_user,begin_time,flow_auto_num) VALUES (run_id, run_name,begin_user, BEGIN_TIME,flow_auto_num)'