@echo off

rem 直接停止 ispirit.exe 进程
taskkill /f /im ispirit.exe > nul 2>&1

rem 检查错误级别，如果错误级别为 0，则表示成功停止进程
if errorlevel 1 (
    echo 无法停止 ispirit.exe 进程。
) else (
    echo ispirit.exe 进程已成功停止。
)

set "mydocuments=%USERPROFILE%\Documents\tongda\ispirit"

echo 我的文档路径：%mydocuments%

rem 遍历目标文件夹，显示名称同时包含指定符号的文件夹
for /f "delims=" %%a in ('dir /b /ad "%mydocuments%" ^| findstr /r /c:".*{.*}.*_.*"') do (
    echo 文件夹名称包含指定符号："%%a"
rd /s /q "%mydocuments%\%%a"
)

pause