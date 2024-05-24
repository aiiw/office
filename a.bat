cd /d "D:\office\"
icacls "D:\office\log.txt" /grant "%USERNAME%:(W)"
echo %date% %time% >> log.txt
@echo off
cd /d "D:\office\"
call ÉÏ´«.bat
rem icacls "C:\Users\11608\Desktop\public" /grant "%USERNAME%:(OI)(CI)(W)" /T