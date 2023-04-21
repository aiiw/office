这个问题可能是由于系统编码和Git编码不一致导致的。你可以尝试在git配置中设置编码来解决这个问题。以下是一些可能有用的命令:

1. 确定文件名编码：

   ```
   Copy Code$ file -i <filename>
   ```

2. 设置 Git 编码：

   ```
   Copy Code$ git config --global core.quotepath false
   $ git config --global gui.encoding utf-8
   $ git config --global i18n.commit.encoding utf-8
   $ git config --global i18n.logoutputencoding utf-8
   ```

3. 将文件名编码转换为 UTF-8 编码：

   ```
   Copy Code$ iconv -f <old_encoding> -t utf-8 <filename> > <new_filename>
   ```

4. 在 Git 中重新添加文件：

   ```
   Copy Code$ git add <new_filename>
   ```

尝试上述步骤后，再次使用 `git status` 命令查看是否已经成功解决了乱码问题。





`git config --global core.quotepath false` 是一个 Git 配置命令，它指示 Git 禁用路径中的引号转义。默认情况下，Git 会将路径中的空格和其他特殊字符转义为 Unicode 转义序列或 C 字符串转义序列。

如果启用了 `core.quotepath`，则 `git status` 命令等会显示类似于下面的输出：

```
Copy Codemodified:   "vue/\345\260\232\350\200\201\345\270\210.md"
```

而如果禁用了 `core.quotepath`，则 `git status` 命令等会显示类似于下面的输出：

```
Copy Codemodified:   vue/文件名.md
```

通过禁用 `core.quotepath`，Git 将路径中的空格和其他特殊字符保留为它们本来的字符，从而更容易阅读和理解 Git 的输出。