 grep -r -I "INSERT INTO sfabuc_t(sfabucent,sfabucsite,sfabucdocno,sfabuc001,sfabuc002,sfabucdocdt)" .

pmds000

 grep -r -I "pmds000" . 

 grep -r -I "xceb001" .



这是一个在Linux或类Unix系统上使用grep命令的命令行语法。

- `grep`: 是一个用于在文件中搜索指定模式的命令。
- `-r`: 表示递归搜索，即在指定目录及其子目录中搜索匹配的模式。
- `-I`: 表示不搜索二进制文件。如果目标文件是二进制文件，grep会忽略它而不搜索其中的内容。
- `"xceb001"`: 是要搜索的模式，即要在文件中查找的字符串。
- `.`: 表示当前目录，即在当前目录及其子目录中搜索。



```
grep -r --include="*4gl*" -I "sfba016" .
```

在这个示例中，`--include="*4gl*"`表示要搜索的文件名模式，其中`*`表示可以匹配任意字符。这样，`grep`命令将只搜索文件名中包含"4gl"两个字符的文件，并且还会排除二进制文件。

请注意，`grep`命令的确切语法可能因操作系统和版本而有所不同。请根据你所使用的系统和`grep`版本来调整命令。





```
grep -r --exclude="*aa*" -I "xceb001" .
```

在这个示例中，`--exclude="*aa*"`表示要排除的文件名模式，即文件名中包含"aa"两个字符的文件。这样，`grep`命令将搜索文件名不包含"aa"两个字符的文件，并且还会排除二进制文件。