```
以下是 Maven 的一些常用命令：

mvn clean：清除 target 目录，删除所有编译生成的文件。
mvn compile：编译源代码。
mvn test：运行测试。
mvn package：打包应用程序。
mvn install：将应用程序安装到本地仓库。
mvn deploy：将应用程序部署到远程仓库。
mvn dependency:tree：显示项目依赖树。
mvn dependency:list：以列表形式显示项目依赖项。
mvn help：显示帮助信息。
mvn version：显示 Maven 版本信息。
还有很多其他的命令，你可以通过输入 mvn --help 来查看所有可用的命令和选项。
```

### 问题:它和npm 差不多吧，有没有初始化的命令

```
mvn archetype:generate -DgroupId=com.example -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

```

### 问题:查看本地仓库:

`mvn help:evaluate -Dexpression=settings.localRepository` 是 Maven 命令行工具的一个命令，用于查看当前 Maven 配置文件中配置的本地存储库路径

```
mvn help:evaluate -Dexpression=settings.localRepository 是 Maven 命令行工具的一个命令，用于查看当前 Maven 配置文件中配置的本地存储库路径
```

### 问题:查看远程仓库

```
mvn help:effective-settings  这个有效果
```

### 问题更改默认本地仓库和中央仓库

```
<settings>
  ...
  #<localRepository>/path/to/local/repo</localRepository>
  <localRepository>e:/mavenrepo</localRepository>

</settings>
```

### 问题:改镜像:

```
 <!-- 阿里云镜像仓库 -->
    <mirror>
      <id>aliyunmaven</id>
      <name>Aliyun Maven</name>
      <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
      <mirrorOf>central</mirrorOf>
    </mirror>
```

