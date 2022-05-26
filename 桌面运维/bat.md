## 增加域账号

```shell
@echo off
set /p b= 请输入前缀:
net localgroup administrators /add mastercn.local\%b%
pause
```

## 显示公告栏

```bat
taskkill /f /im explorer.exe >nul 2>nul
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer /v EnableAutoTray /t REG_DWORD /d 0 /f
start "" explorer
```

## 输入与运行

```bat
@echo off
set /p b=输入一个数字：
echo %b%
set /a a=2*%b%
echo %a%
echo %b%+%b%=%a%
setlocal ENABLEDELAYEDEXPANSION
set /a sum=0
set /a ii=0
for /l %%i in (1,1,100) do (
set /a ii+=1
echo !ii!
set /a sum+=!ii!
)
echo !sum!
pause>nul

```

## 定时删除文件

```bat
@echo off

echo 删除60天前的.bak文件和日志

forfiles /p "D:\Backup" /m *.bak /d -63 /c "cmd /c del @path"

echo 正在执行逻辑删除，请稍等……


echo 任务完成! 

```

## 变量延迟

```bat
@12121
for /l %%a in (1,1,10) do (
      set /a Num+=2
      echo %Num%
)
pause


@echo off
setlocal enabledelayedexpansion
for /l %%a in (1,1,10) do (
      set /a Num+=2
      echo !Num!
)
pause


set var1=test1 & echo %test%
pause
for /l %%i in (1,1,5) do (
    set var=123
    echo %var%
)
pause

@echo off
set var=test
for /l %%i in (1,1,5) do (
    set var=%%i
    echo %var%
)
pause
```

## 获取别人提供的ip

```bat
@echo off
color 1F
title 请求远程协助脚本
set name=%username%
set filename=%name%.txt

:home
cls
echo.
echo 请右击「以管理员身份运行」
echo.
echo.
echo         1、开启远程协助
echo.
echo         2、关闭远程协助
echo.
echo         0、退出
echo.
echo.

set /p num=请输入：
if %num%==1 goto 1
if %num%==2 goto 2
if %num%==0 goto 0

:1
cls
echo.
echo ================================================
echo.
net start SessionEnv
net start TermService
::开启远程桌面
netsh firewall set opmode mode = disable>%temp%\result.tmp
if %errorlevel%==0 (echo 已关闭防火墙。) else (echo 关闭防火墙失败。)
echo.
::关闭防火墙
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
::配置注册表，开启选项
echo.
echo ================================================
echo.
echo.
set /p pass=请输入电脑密码：
echo 账号：%username% >%temp%\%filename%
echo 密码：%pass% >>%temp%\%filename%
ipconfig | findstr "192.168.4" >%temp%\ip.tmp
set /p a=<%temp%\ip.tmp
echo IP：%a:~-14% >>%temp%\%filename%
::截取IP地址
echo. 

copy %temp%\%filename% \\192.168.4.253\yy\
::复制电脑信息到共享
echo.
if %errorlevel%==0 (echo 管理员已收到信息，等待处理。) else (echo 发送信息失败。)
del %temp%\ip.tmp && del %temp%\result.tmp
::删除临时文件

echo.
pause&exit

:2
cls
echo.
echo 开始配置...
echo.
sc config MpsSvc start= auto
sc config SessionEnv start= demand
sc config TermService start= demand
::设置开机服务
netsh firewall set opmode mode = enable>%temp%\result.tmp
if %errorlevel%==0 (echo 已开启防火墙。) else (echo 开启防火墙失败。)
del %temp%\result.tmp
::开启防火墙
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f
::配置注册表，关闭选项
echo.
pause&exit

:0
exit
```

## 获取用户名

```bat
@echo off
echo 本机上拥有以下用户：
echo.
for /f "skip=4 tokens=1-3" %%i in ('net user') do (
    if not "%%i"=="命令成功完成。" echo %%i
    if not "%%j"=="" echo %%j
    if not "%%k"=="" echo %%k 555
)
echo.
echo 当前登录本机的账户是：%username%
pause>nul

```

## 开防火墙策略

```bat
set PORT=3389
set RULE_NAME="_远程连接端口：%PORT% 入栈规则"
netsh advfirewall firewall show rule name=%RULE_NAME% >nul
if not ERRORLEVEL 1 (
    rem 对不起，规则 %RULENAME% 已经存在
) else (
    echo 规则 %RULENAME% 创建中...
    netsh advfirewall firewall add rule name=%RULE_NAME% dir=in action=allow protocol=TCP localport=%PORT%
) 

出栈规则：
set PORT=3389
set RULE_NAME="_远程连接端口：%PORT% 出栈规则"
netsh advfirewall firewall show rule name=%RULE_NAME% >nul
if not ERRORLEVEL 1 (
    rem 对不起，规则 %RULENAME% 已经存在
) else (
    echo 规则 %RULENAME% 创建中...
    netsh advfirewall firewall add rule name=%RULE_NAME% dir=outaction=allow protocol=TCP localport=%PORT%
) 
pause

```



## 字符串的提取

```bat
@echo off
　　set aa=%date%
　　echo 替换前：%aa%
　　echo 替换后：%aa:/=%

      echo 截取字符

　　set ifo=abcdefghijklmnopqrstuvwxyz0123456789
　　echo 原字符串（第二行为各字符的序号）：
　　echo %ifo%
　　echo 123456789012345678901234567890123456
　　echo 截取前5个字符：
　　echo %ifo:~0,5%
　　echo 截取最后5个字符：
　　echo %ifo:~-5%
　　echo 截取第一个到倒数第6个字符：
　　echo %ifo:~0,-5%
　　echo 从第4个字符开始，截取5个字符：
　　echo %ifo:~3,5%
　　echo 从倒数第14个字符开始，截取5个字符：
　　echo %ifo:~-14,5%

      echo 替换字符串

      set aa=伟大的中国！我为你自豪！
　　echo 替换前：%aa%
　　echo 替换后：%aa:中国=中华人民共和国%
　　echo aa = %aa%
　　set "aa=%aa:中国=中华人民共和国%"
　　echo aa = %aa%

      echo 字符串合并

      @echo off
　　set aa=伟大的中国！
　　set bb=我为你自豪！
　　echo %aa%%bb%
　　echo aa=%aa%
　　echo bb=%bb%
　　set "aa=%aa%%bb%"
　　echo aa=%aa%

      echo 扩充字符串
      @echo off
　　echo 正在运行的这个批处理：
　　echo 完全路径：%0
　　echo 去掉引号：%~0
　　echo 所在分区：%~d0
　　echo 所处路径：%~p0
　　echo 文件名：%~n0
　　echo 扩展名：%~x0
　　echo 文件属性：%~a0
　　echo 修改时间：%~t0
　　echo 文件大小：%~z0
　　pause
     
　　pause
```

