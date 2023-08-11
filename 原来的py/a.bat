cd /d "D:\py\"
icacls "D:\py\log.txt" /grant "%USERNAME%:(W)"
echo %date% %time% >> log.txt
@echo off
call ио╢╚.bat