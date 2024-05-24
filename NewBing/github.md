这个报错是由于你使用的 RSA 密钥哈希算法是 SHA-1，而 GitHub 已经禁止使用 SHA-1 算法进行认证。为了解决这个问题，你需要升级到一个支持更强密钥哈希算法的 Git 版本或者生成一个新的 SSH 密钥对。

为了生成新的密钥对，请按照以下步骤操作：

1. 打开终端并运行以下命令，以验证是否存在 SSH 密钥：

   ```
   Copy Codels -al ~/.ssh
   ```

2. 如果你没有找到 `id_rsa` 和 `id_rsa.pub` 这两个文件，请运行以下命令生成一对新的 SSH 密钥：

   ```
   Copy Codessh-keygen -t ed25519 -C "your_email@example.com"
   ```

   在运行上述命令时，请使用你的电子邮件地址替换 `your_email@example.com`。

3. 将新生成的公钥 `id_rsa.pub` 添加到你的 GitHub 帐户中。你可以在帐户设置页面的 SSH 和 GPG 密钥部分中添加它。

   复制 `id_rsa.pub` 的内容，并将其粘贴到 GitHub 网站上的新 SSH 密钥表单中。

4. 确认已将 SSH 密钥添加到 GitHub 帐户后，请再次运行 `git push` 命令。

如果你升级到了最新版的 Git 但仍然遇到该问题，可以尝试使用以下命令清除现有的 SSH 密钥缓存：



# 如上是生成一个密钥文件：id_rsa.pub

## 将如上文件的内容，放在GITHUB网站的新的ssh。



非常对，提交时可以指定多个文件或者提交整个工作目录的所有变更。以下是一些相关的 Git 命令：

1. `git add .`：将所有修改过的文件添加到暂存区。
2. `git commit -m "<message>"`：提交所有在暂存区中的修改。
3. `git commit <file1> <file2> ... -m "<message>"`：提交指定的文件并包含提交消息描述。
4. `git commit -a -m "<message>"`：将所有已跟踪的文件的修改都提交到本地仓库。

这些命令允许你在一个提交中处理多个文件的修改，而无需单独为每个文件创建单独的提交。请注意，`git add .` 和 `git commit -a` 命令可能会将您不想提交的更改添加到 Git 仓库中，因此请谨慎使用。

```
好的，以下是一些更实用、常用的 Git 命令：

git init：初始化一个新的 Git 仓库。
git clone <url>：从远程 Git 仓库克隆项目。
git add <file>：将指定文件添加到 Git 暂存区。
git commit -m "<message>"：提交暂存区中的文件，并附加提交消息描述。
git status：显示当前工作目录状态，包括已修改但未提交的文件等。
git log：查看 Git 提交日志。
git branch：列出所有本地分支。
git checkout <branch>：切换到指定分支。
git merge <branch>：将指定分支合并到当前分支。
git push <remote> <branch>：将本地分支推送到远程仓库。
git pull <remote> <branch>：从远程仓库拉取最新代码。
git remote -v：列出所有远程仓库。
git diff：比较工作目录和暂存区之间的差异。
git tag <tagname>：为当前提交打上标签。
git stash：将当前工作目录的变更保存到 Git 堆栈中，以便稍后恢复。
git reset <file>：取消对文件的暂存操作，使其不包含在下一次提交中。
git revert <commit>：撤销指定提交的修改，并创建一个新的提交来反映这个更改。
git fetch：从远程仓库下载最新的提交，但不会将其合并到本地分支。
git cherry-pick <commit>：将指定提交中的变更应用到当前分支中。
git rm <file>：从 Git 仓库中删除文件。
这些是常用的 Git 命令，可以帮助你完成大多数 Git 操作。如果需要更高级的 Git 功能，则可能需要查阅 Git 文档或参考其他资源。
```

