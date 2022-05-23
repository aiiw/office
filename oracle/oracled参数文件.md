oracle数据库的配置文件指的是系统在启动到“nomount”阶段需要加载的文件，也叫做pfile或者spfile，但是其实pfile和spfile是不同的文件。
配置文件分两种，一种叫pfile，一种叫spfile，区别在于spfile是二进制文件，给机器看的，pfile是文本文件，给用户看的，但是oracle启动的时候只会加载其中一个文件，当然最好是加载二进制的spfile，速度更快。
虽然配置文件分两种，但是文件里的配置，或者说文件想表达的内容是一样的，所以这两个文件是可以相互转换的

spfile文件命名规则：” SPFILE” +sid. ora；例如SPFILEORCL.ORA
pfile文件命名规则：” INIT”+ sid. ora；例如INITorcl.ORA

可能大多数朋友发现，在存放配置文件的文件夹里，只有spfile，没有pfile，本人电脑上的数据库是刚安装的64位oracle，也是没有，那么想要数据库用文本文件启动，或者想用文本文件查看下配置文件的参数，却又没有这个文件怎么办呢，命令oracle以spfile文件的配置生成一个pfile就可以了，输入以下命令：
create pfile from spfile;
提示文本文件已创建。
再次查看文件夹会发现已存在pfile文件

3. 让oracle加载pfile或者spfile
系统默认用二进制文件启动，但是有的朋友喜欢用文本文件启动，方便查看实时的参数。这里说明下，系统无法修改用哪种参数文件启动（个人猜测是因为参数文件是oracle启动时加载的第一个文件，如果这个文件可以随意配置，会导致无法启动等故障）。但是oracle对参数文件有一个加载顺序，优先查找加载spfile，找不到再去找pfile，所以我们可以生成了pfile后将spfile文件删除，这样系统就自动加载pfile了 ，这时候再去执行spfile命令，查到的结果就是空（加载的一定是pfile文件 ，如果没有加载任何文件的话，数据库无法启动）