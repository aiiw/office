```
echo "# mypy" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main  #本地的别名
git remote add origin git@github.com:aiiw/mypy.git   #  origin 远程的别名
git push -u origin main #上传
```

git add . 表示添加新文件和编辑过的文件不包括删除的文件; git add -u 表示添加编辑或者删除的文件，不包括新添加的文件

git commit -m "提交注释"



问题坑:
https://blog.csdn.net/lishuangquan1987/article/details/123588802

![image-20220526175503177](C:/Users/11608/AppData/Roaming/Typora/typora-user-images/image-20220526175503177.png)
