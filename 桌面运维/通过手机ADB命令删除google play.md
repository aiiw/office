## 								通过手机ADB命令删除google play

### 1 前提:手机可以连接到PC,并且打开了USB的调试模式

### 2 下载:ADB工具(windows)

https://dl.google.com/android/repository/platform-tools-latest-windows.zip



### 3 adb shell pm list packages |find "goo"

![image-20240607103020366](https://gitee.com/aiiw/images/raw/master/img/image-20240607103020366.png)

### 4 adb shell pm uninstall -k --user 0 com.google.android.gms

adb shell pm uninstall -k --user 0 com.google.android.ext.services

![image-20240607103156302](https://gitee.com/aiiw/images/raw/master/img/image-20240607103156302.png)

### 5 问题:

```
adb shell pm uninstall com.google.android.gms
Failure [DELETE_FAILED_DEVICE_POLICY_MANAGER]
====++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++====
解决:在设备-安全-设备管理器,将带有激活的全部取消,就可以解决了.
```

### 6 附带ADB命令

```
adb version ：显示 adb 版本
adb help：帮助信息，查看adb所支持的所有命令
adb devices：查看当前连接的设备，已连接的设备会显示出来
adb get-serialno：也可以查看设备号
adb shell：登录设备 shell，该命令将登录设备的shell（内核），登录shell后，可以使用 cd，ls，rm 等Linux命令
adb shell pm list packages：列出当前设备/手机，所有的包名
adb install -d <文件路径\apk>：允许降级覆盖安装
adb install -g <文件路径\apk>：授权/获取权限，安装软件时把所有权限都打开
adb uninstall <包名>：卸载该软件/app。
adb shell getprop ro.product.model：获取设备型号
adb get-serialno：获取设备的序列号（设备号）
adb shell wm size：获取设备屏幕分辨率
adb shell cat /proc/meminfo：获取手机内存信息
adb shell df：获取手机存储信息
```

### 7其他

```
如果设备没有被 root，那么通过adb连接到设备时所能执行的操作会受到一定的限制。一般情况下，没有root权限的设备上，通过adb可以执行的操作包括文件的查看、复制、删除，安装和卸载应用程序，发送shell命令等。

但是，如果你想要执行一些需要更高权限的操作，比如修改系统文件或者访问某些受限目录，那么就需要设备被root，并通过su命令获取root权限。在设备没有被root的情况下，确实会受到一些权限限制。
```

