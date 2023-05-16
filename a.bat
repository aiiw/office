icacls "D:\office\log.txt" /grant "%USERNAME%:(W)"
echo %date% %time% >> log.txt
@echo off
cd /d "D:\office\"
call ио╢╚.bat