要解决 `git status` 命令显示中文乱码的问题，你可以尝试以下方法：

1. **设置字符编码**：首先，确保你的终端的字符编码设置正确。你可以尝试将终端的字符编码设置为 UTF-8 或者 GBK，以确保能够正确显示中文字符。在 CMD 终端下，可以使用 `chcp 65001` 切换到 UTF-8 编码。

2. **配置 Git**：你可以通过配置 Git 来告诉它如何处理文件名和文件内容的编码。在命令行中执行以下命令来设置 Git 使用 GBK 编码：

   ```
   Copy Codegit config --global core.quotepath false
   git config --global gui.encoding gbk
   git config --global i18n.commit.encoding gbk
   git config --global i18n.logoutputencoding gbk
   ```

   这样设置后，Git 应该能够正确地显示中文文件名和内容。

3. **使用 Git Bash**：如果在 CMD 终端中无法解决问题，可以尝试使用 Git 自带的 Bash 终端。Git Bash 对字符编码的支持通常更好，能够更好地显示中文字符。

4. **检查文件名编码**：确保文件名的编码是正确的。如果文件名的编码不正确，可能会导致 `git status` 显示乱码。你可以使用文件资源管理器或者命令行工具来检查和更改文件名的编码。

通过以上方法，你应该能够解决 `git status` 显示中文乱码的问题。如果问题仍然存在，可能需要进一步调查和调试。





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