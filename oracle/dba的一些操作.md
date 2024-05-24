```
sqlplus / as sysdba
如果登录系统的账号不是数据库账号,会提示连接到一个空的数据库

create user xxzx01 identified by xxzx01
alter user xxzx01 account unlock
grant dba to xxzx01;


lsnrctl status

LSNRCTL for Linux: Version 12.2.0.1.0 - Production on 17-FEB-2023 15:03:30

Copyright (c) 1991, 2016, Oracle.  All rights reserved.

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=bpm-db)(PORT=1521)))
STATUS of the LISTENER
------------------------
Alias                     LISTENER
Version                   TNSLSNR for Linux: Version 12.2.0.1.0 - Production
Start Date                12-FEB-2023 09:39:35
Uptime                    5 days 5 hr. 24 min. 5 sec
Trace Level               off
Security                  ON: Local OS Authentication
SNMP                      OFF
Listener Parameter File   /u2/oracle/product/12.2.0/dbhome_1/network/admin/listener.ora
Listener Log File         /u2/oracle/diag/tnslsnr/dwh/listener/alert/log.xml
Listening Endpoints Summary...
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=dwh)(PORT=1521)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC1521)))
Services Summary...
Service "pentaho" has 1 instance(s).
  Instance "pentaho", status READY, has 1 handler(s) for this service...
Service "pentahoXDB" has 1 instance(s).
  Instance "pentaho", status READY, has 1 handler(s) for this service...
The command completed successfully



 lsnrctl start


select * from v$version;
```

