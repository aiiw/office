<?
//通达OA自动发起工作流代码
include_once("inc/conn.php");
$wenhao="XXX的申请";//文号标题
$faqiren="admin";//发起人
$jieshouren="lijia";//下一步接收人
$fqsj="2014-11-16 21:16:27";//发起时间
$jssj="2014-11-16 21:16:27";//接收时间
$flow_id="11";//流程ID

$zd="data_1,data_2";//字段
$zdz="11,22";//字段值

$rid=mysql_fetch_array(exequery( TD::conn( ),"select max(run_id) from `flow_run` "));
$run_id=$rid[0]+1;//run_id

$sql1="INSERT INTO `flow_run`  VALUES ('$run_id', '$wenhao', '11', '$faqiren', '2', '$fqsj', null, '', '', '0', '', '0', '', '', '', '', '0', '', '0')";
exequery( TD::conn( ),$sql1);


$sql2="INSERT INTO `flow_data_11` (run_id,run_name,begin_user,begin_time,flow_auto_num,$zd) VALUES ('$run_id', '$wenhao', '$faqiren', '$fqsj', '0', $zdz)";
exequery( TD::conn( ),$sql2);


//流程日志
//INSERT INTO `flow_run_log` VALUES (null, '1', '$wenhao', '11', '1', '1', '$faqiren', '$jssj', '127.0.0.1', '1', '转交至步骤2,办理人:李佳,', '0');

$sql3="INSERT INTO `flow_run_prcs` VALUES (null, '$run_id', '1', '$faqiren', '$fqsj', '$jssj', '3', '1', '1', '0', '0', '0', '', '', '', '', '0', '$fqsj', '', '0000-00-00 00:00:00', '', '2', '0', '0', '0', '0', '0', '', '')";
exequery( TD::conn( ),$sql3);

$sql4="INSERT INTO `flow_run_prcs` VALUES (null, '$run_id', '2', '$jieshouren', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '1', '2', '1', '0', '1', '0', '', '', '', ',', '0', '2014-11-16 21:17:02', '', '0000-00-00 00:00:00', '', '17', '1', '0', '0', '0', '0', '', '')";
exequery( TD::conn( ),$sql4);