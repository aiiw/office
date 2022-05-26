# git

### git与github

##### 选择一个文件夹,git init 初始为本地仓库 ,执行如下命令会第一次上传文件到github

```
echo "# mypy" >> README.md
git init
git add README.md
git add #提交所有到暂存区
git commit -m "first commit"
git branch -M main  #本地的别名
git remote add origin git@github.com:aiiw/mypy.git   #  origin 远程的别名
git push -u origin main
```

### 后期可以通过如下,上传

```
git status
git add .
git commit -m "first commit"
git push -u origin main
pause
```

或者

```
git status
git add .
git commit -m "first commit"
git pull origin
git push -u origin main
pause
```

配置github

| 查看配置::::::::::::::::::::git config  --global --list      |
| ------------------------------------------------------------ |
| 配置邮    箱::::::::::::::::::git config --global user.email "[gitHub](https://so.csdn.net/so/search?q=gitHub&spm=1001.2101.3001.7020)邮箱" |
| 配置用户名::::::::::::::::: git config --global user.name "gitHub用户名" |



```
echo. >> C:\Windows\System32\drivers\etc\hosts 
echo 20.205.243.166 github.com >> C:\Windows\System32\drivers\etc\hosts 
pause
```

```
$ ssh-keygen -t ed25519 -C "your_email@example.com"
```

生成之后，会在本地生成两个文件：

- id_ed25519
- id_ed25519.pub

### 将id_ed25519.pub添加到github 的 ssh,只保留一个就行了

| 测试功能:::::::::::::::::::::ssh -t  git@github.com   (相当了 ssh -t 主机) |
| ------------------------------------------------------------ |



# 如下为摘录网上的资料

# Git 工作区、暂存区和版本库

------

## 基本概念

我们先来理解下 Git 工作区、暂存区和版本库概念：

- **工作区：**就是你在电脑里能看到的目录。
- **暂存区：**英文叫 stage 或 index。一般存放在 **.git** 目录下的 index 文件（.git/index）中，所以我们把暂存区有时也叫作索引（index）。
- **版本库：**工作区有一个隐藏目录 **.git**，这个不算工作区，而是 Git 的版本库。

下面这个图展示了工作区、版本库中的暂存区和版本库之间的关系

![img](https://gitee.com/aiiw/images/raw/master/img/1352126739_7909.jpg)

![img](https://gitee.com/aiiw/images/raw/master/img/git-command.jpg)

**说明：**

- workspace：工作区
- staging area：暂存区/缓存区
- local repository：版本库或本地仓库
- remote repository：远程仓库

### 创建仓库命令

下表列出了 git 创建仓库的命令：

| 命令        | 说明                                   |
| :---------- | :------------------------------------- |
| `git init`  | 初始化仓库                             |
| `git clone` | 拷贝一份远程仓库，也就是下载一个项目。 |

------

## 提交与修改

Git 的工作就是创建和保存你的项目的快照及与之后的快照进行对比。

下表列出了有关创建与提交你的项目的快照的命令：

| 命令         | 说明                                     |
| :----------- | :--------------------------------------- |
| `git add`    | 添加文件到暂存区                         |
| `git status` | 查看仓库当前的状态，显示有变更的文件。   |
| `git diff`   | 比较文件的不同，即暂存区和工作区的差异。 |
| `git commit` | 提交暂存区到本地仓库。                   |
| `git reset`  | 回退版本。                               |
| `git rm`     | 删除工作区文件。                         |
| `git mv`     | 移动或重命名工作区文件。                 |

### 提交日志

| 命令               | 说明                                 |
| :----------------- | :----------------------------------- |
| `git log`          | 查看历史提交记录                     |
| `git blame <file>` | 以列表形式查看指定文件的历史修改记录 |

### 远程操作

| 命令         | 说明               |
| :----------- | :----------------- |
| `git remote` | 远程仓库操作       |
| `git fetch`  | 从远程获取代码库   |
| `git pull`   | 下载远程代码并合并 |
| `git push`   | 上传远程代码并合并 |

![](C:/Users/11608/AppData/Roaming/Typora/typora-user-images/image-20220526210328388.png)