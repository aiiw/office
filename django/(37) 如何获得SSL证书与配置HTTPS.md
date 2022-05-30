# 基础(37): 如何获得SSL证书与配置HTTPS

**为什么你的网站需要支持HTTPS协议?**

简而言之：**HTTPS = HTTP + SSL = 更安全的数据传输**

HTTP协议简称超文本传输协议，它广泛用于在Web浏览器和网站服务器之间传递信息。HTTP协议的缺点是它以明文方式发送内容（包括用户密码)，不提供任何方式的数据加密。如果攻击者截取了Web浏览器和网站服务器之间的传输文本，就可以直接读取其中的信息。

为了解决这个隐患和保证数据的传输安全，HTTPS协议(安全套接字层超文本传输协议)诞生了。它在HTTP的基础上加入了SSL协议，SSL依靠证书来验证服务器的身份，并为浏览器和服务器之间的通信数据加密。

注意：HTTP协议默认使用的端口是80端口，HTTPS协议默认使用的端口是443端口。如果你使用云服务器，请确保设置安全组时已经开放了443端口。



**如何在生产环境中部署Django项目时配置HTTPS?**

一共分三步：

1. 购买下载SSL证书，通常包括一张证书(.cert或.pem)和一个私有密钥文件(.key)。

2. 修改Nginx或Apache配置信息，并上传下载颁发的SSL证书及key到指定文件夹

3. 修改Django配置文件settings.py



**第一步：购买下载SSL证书**

SSL证书有很多种, 级别越高越贵，网上的免费午餐并不多。对于个人网站使用单域名的DV SSL证书一般就够了，这种证书阿里云做活动期间是可以免费申请的。购买SSL证书时选择单域名-DV SSL-免费版即可，如下图所示。收费版的SSL证书价格比较便宜的还namecheap。

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoDeX0x8YHM552lS1mHrpcbOVqUdwZvsoRkWKI7td7ZHcOYpibUUHfMyIXzicFGHRVtcn1mcIBf3nA0w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

无论哪个SSL证书服务商最后都会提供证书下载链接或直接将证书发送到你的邮箱，只是流程不同而已。随后你需要将下载的证书上传到服务器指定文件夹，见下一步。



**第二步：修改Nginx配置信息**

在生产环境中部署Django时我们一般以Nginx做反向代理和静态文件服务器，这里简单说下Nginx的配置信息。Nginx配置文件通常位于*/etc/nginx/conf.d*目录下，修改配置文件添加SSL相关信息。

```
# /etc/nginx/conf.d目录下的配置文件server {listen 443 ssl; 监听443端口ssl_certificate /path/to/certificate/your_domain_chain.crt; # 证书地址ssl_certificate_key /path/to/your_private.key; # 私有密钥文件地址server_name your_domain.com www.your_domain.com; # 域名}
```

SSL证书和私有密钥文件可以上传到服务器上任何一个指定目录，但通常做法是将其上传到Linux的*/usr/share/nginx/ssl*目录下，所以上述配置信息可以简化为：

```
# /etc/nginx/conf.d目录下的配置文件server {listen 443 ssl; 监听443端口ssl_certificate /usr/share/nginx/ssl/your_domain_chain.crt; # 证书地址ssl_certificate_key /usr/share/nginx/ssl/your_private.key; # 私有密钥文件地址server_name your_domain.com www.your_domain.com; # 域名}
```

你还可以将所有来自80端口的http请求永久地重定向至https。

```
server {listen 80; # 监听80端口server_name your_domain.com www.your_domain.com;return 301 https://$server_name$request_uri; # 永久重定向}
```

**第三步 修改Django的settings.py**

当你的网站支持https后，你可以在settings.py新增如下安全配置，可以给网站和用户数据提供更高级别的保护。这个设置也是django cookiecutter推荐的在生产环境中的默认配置。

```
# SECURITY安全设置 - 支持http时建议开启SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")SECURE_SSL_REDIRECT = True # 将所有非SSL请求永久重定向到SSLSESSION_COOKIE_SECURE = True # 仅通过https传输cookieCSRF_COOKIE_SECURE = True # 仅通过https传输cookieSECURE_HSTS_INCLUDE_SUBDOMAINS = True # 严格要求使用https协议传输SECURE_HSTS_PRELOAD = True # HSTS为SECURE_HSTS_SECONDS = 60SECURE_CONTENT_TYPE_NOSNIFF = True # 防止浏览器猜测资产的内容类型
```

**注意**：Django的SECURE_SSL_REDIRECT = True也可实现80端口的http请求永久地重定向至https, 与Nginx的301重定向设置选其一即可。Django以上的几个安全设置均依赖下面这个SecurityMiddleware中间件。

```
MIDDLEWARE = [    'django.middleware.security.SecurityMiddleware',]
```


**小结**

Django项目上线时配置https非常简单，仅需3步。你学会了吗?