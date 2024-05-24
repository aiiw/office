### 1注册一个百度账号并创建应用程序

在开始之前，你需要先在百度上注册一个账号（如果你还没有）并创建一个新的应用程序。创建应用程序时，你需要填写一些基本信息，并为应用程序分配一个客户端 ID 和客户端秘钥。这些信息将在后面的步骤中用到。

### 2配置回调地址

在创建应用程序后，你需要在应用程序设置中配置回调地址。回调地址是一个接收授权码并用它来换取访问令牌的页面 URL，因此你需要将其设置为一个可公开访问的 URL。

例如，你可以将回调地址设置为 `http://localhost:3000/oauth_callback` （其中 `3000` 是你的 Web 服务器端口号），或者将其设置为你的生产环境 URL（例如 `https://example.com/oauth_callback`）。

### 3发起 OAuth2.0 授权请求

现在你可以在你的 Web 应用程序中发起 OAuth2.0 授权请求。通常情况下，你需要提供一个登录按钮或链接，以便用户点击该按钮或链接来启动授权流程。例如，在 Vue.js 中，你可以定义一个简单的登录组件，如下所示：

```vue
<template>
  <div class="oauth-callback">
    <h1>处理授权码</h1>

    <!-- 显示加载状态 -->
    <div v-if="isLoading">正在加载...</div>

    <!-- 显示错误消息 -->
    <div v-if="errorMessage">{{ errorMessage }}</div>

    <!-- 显示访问令牌 -->
    <div v-if="accessToken">Access Token: {{ accessToken }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLoading: true,
      errorMessage: null,
      accessToken: null,
    };
  },

  mounted() {
    const clientId = 'your-client-id'; // 将其替换为你的客户端 ID
    const clientSecret = 'your-client-secret'; // 将其替换为你的客户端秘钥
    const redirectUri = 'http://localhost:3000/oauth_callback'; // 将其替换为你的回调地址 URL
    const storageKey = 'baiduOAuth2Tokens'; // 本地存储键名

    // 从 URL 参数中解析授权码
    const params = new URLSearchParams(window.location.search);
    const code = params.get('code');

    // 获取或创建本地存储中的令牌数据
    let tokens = JSON.parse(localStorage.getItem(storageKey)) || {};

    // 如果本地存储中已有访问令牌，并且它没有过期，则使用它
    if (tokens.access_token && new Date(tokens.expires_at) > new Date()) {
      this.accessToken = tokens.access_token;
      this.isLoading = false;

      // 设置刷新定时器
      setTimeout(() => {
        this.refreshToken(clientId, clientSecret, redirectUri, storageKey);
      }, tokens.expires_in * 1000 - 60000); // 提前一分钟刷新令牌

      return;
    }

    // 否则，向服务器请求访问令牌
    fetch('/api/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code }),
    })
      .then(response => response.json())
      .then(data => {
        // 处理访问令牌
        this.isLoading = false;
        this.accessToken = data.access_token;

        // 存储访问令牌和刷新令牌到本地存储
        tokens.access_token = data.access_token;
        tokens.refresh_token = data.refresh_token;
        tokens.expires_in = data.expires_in;
        tokens.expires_at = new Date(Date.now() + data.expires_in * 1000).toISOString();
        localStorage.setItem(storageKey, JSON.stringify(tokens));

        // 设置刷新定时器
        setTimeout(() => {
          this.refreshToken(clientId, clientSecret, redirectUri, storageKey);
        }, data.expires_in * 1000 - 60000); // 提前一分钟刷新令牌
      })
      .catch(error => {
        // 处理错误情况
        this.isLoading = false;
        this.errorMessage = error.message;
      });
  },

  methods: {
    refreshToken(clientId, clientSecret, redirectUri, storageKey) {
      let tokens = JSON.parse(localStorage.getItem(storageKey)) || {};

      // 如果本地存储中已有刷新令牌，并且它没有过期，则使用它更新访问令牌
      if (tokens.refresh_token && new Date(tokens.refresh_expires_at) > new Date()) {
        fetch('/api/refresh', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            grant_type: 'refresh_token',
            refresh_token: tokens.refresh_token,
            client_id: clientId,
            client_secret: clientSecret,
            redirect_uri: redirectUri,
          }),
        })
          .then(response => response.json())
          .then(data => {
            // 更新访问令牌和过期时间
              },

  methods: {
    refreshToken(clientId, clientSecret, redirectUri, storageKey) {
      let tokens = JSON.parse(localStorage.getItem(storageKey)) || {};

      // 如果本地存储中已有刷新令牌，并且它没有过期，则使用它更新访问令牌
      if (tokens.refresh_token && new Date(tokens.refresh_expires_at) > new Date()) {
        fetch('/api/refresh', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            grant_type: 'refresh_token',
            refresh_token: tokens.refresh_token,
            client_id: clientId,
            client_secret: clientSecret,
            redirect_uri: redirectUri,
          }),
        })
          .then(response => response.json())
          .then(data => {
            // 更新访问令牌和过期时间
            tokens.access_token = data.access_token;
            tokens.expires_in = data.expires_in;
            tokens.expires_at = new Date(Date.now() + data.expires_in * 1000).toISOString();
            localStorage.setItem(storageKey, JSON.stringify(tokens));

            // 设置下一次刷新定时器
            setTimeout(() => {
              this.refreshToken(clientId, clientSecret, redirectUri, storageKey);
            }, data.expires_in * 1000 - 60000); // 提前一分钟刷新令牌

            // 更新当前组件的访问令牌
            this.accessToken = data.access_token;
          })
          .catch(error => {
            console.error(error);
          });
      } else {
        // 否则，跳转到授权页面重新获取访问令牌
        window.location.href = `https://oauth.baidu.com/authorize?response_type=code&client_id=${clientId}&redirect_uri=${encodeURIComponent(redirectUri)}`;
      }
    },
  },
};
</script>
```

在第 4 步中的后端 API 中，我们将添加一个用于刷新令牌的路由处理程序。该处理程序将检查请求是否包含正确的参数，并使用百度 OAuth2 的 /token API 来获取新的访问令牌和刷新令牌。

```vue
const express = require('express');
const fetch = require('node-fetch');

const router = express.Router();

router.post('/refresh', async (req, res) => {
  const { grant_type, refresh_token, client_id, client_secret, redirect_uri } = req.body;

  // 检查请求参数是否完整
  if (!grant_type || !refresh_token || !client_id || !client_secret || !redirect_uri) {
    return res.status(400).json({ error: '请求参数不完整' });
  }

  try {
    // 向百度 OAuth2 的 /token API 发送 POST 请求来获取新的访问令牌和刷新令牌
    const response = await fetch(`https://oauth.baidu.com/token?grant_type=${grant_type}&refresh_token=${refresh_token}&client_id=${client_id}&client_secret=${client_secret}&redirect_uri=${encodeURIComponent(redirect_uri)}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
    });

    if (!response.ok) {
      throw new Error('获取访问令牌失败');
    }

    const data = await response.json();

    // 返回新的访问令牌和刷新令牌
    res.json({
      access_token: data.access_token,
      refresh_token: data.refresh_token,
      expires_in: data.expires_in,
    });
  } catch (error) {
    console.error(error);

    res.status(500).json({ error: '服务器出错' });
  }
});

module.exports = router;
```





### 5:关于第三步,还有一个html的例子:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>使用百度账号登录开发者应用</title>
</head>
<body>
  <h1>使用百度账号登录开发者应用</h1>
  <button onclick="login()">登录</button>
  <script src="https://passport.baidu.com/passApi/js/uni_login_wrapper.js"></script>
  <script>
    // 设置 API Key 和回调地址
    var api_key = 'MqTM8icss9Th4pZEdMDmDPeRPti90tzK';
    var redirect_uri = 'http://localhost:8000/callback';

    // 第1步：检查用户是否已经登录百度账号
    function checkLogin() {
      return new Promise(function(resolve, reject) {
        BaiduPassport.getLoginStatus({
          onSuccess: function(status) {
            if (status.isLogin) {
              // 如果用户已经登录，则直接跳过第2步，并返回 Access Token
              resolve(status.accessToken);
            } else {
              // 如果用户未登录，则执行第2步和后续流程
              reject();
            }
          },
          onFailure: function() {
            // 检查登录状态失败，需要执行第2步和后续流程
            reject();
          }
        });
      });
    }

    // 第2步：构建授权页面 URL
    function buildAuthUrl() {
      var auth_url = 'https://openapi.baidu.com/oauth/2.0/authorize' +
        '?response_type=code' +
        '&client_id=' + api_key +
        '&redirect_uri=' + encodeURIComponent(redirect_uri);
      return auth_url;
    }

    // 第3步：打开授权页面进行登录
    function openAuthPage() {
      var auth_url = buildAuthUrl();
      BaiduPassport.login({
        onSuccess: function (response) {
          if (response && response.code) {
            // 如果用户点击了“同意授权”按钮，则通过授权码 Code 换取 Access Token
            exchangeCodeForAccessToken(response.code);
          } else {
            // 用户取消授权
            console.error('用户取消授权');
          }
        },
        onCancel: function () {
          // 用户取消授权
          console.error('用户取消授权');
        },
        onError: function (err) {
          // 登录出错
          console.error('登录失败', err);
        },
        authUrl: auth_url
      });
    }

    // 第4步：通过授权码 Code 换取 Access Token
    function getAccessToken(code) {
      return new Promise(function(resolve, reject) {
        var token_url = 'https://openapi.baidu.com/oauth/2.0/token';
        var params = {
          'grant_type': 'authorization_code',
          'code': code,
          'client_id': api_key,
          'redirect_uri': redirect_uri,
        };
        var xhr = new XMLHttpRequest();
        xhr.open('POST', token_url);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange = function() {
          if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
              try {
                var data = JSON.parse(xhr.responseText);
                var access_token = data.access_token;
                resolve(access_token);
              } catch (err) {
                reject(err);
              }
            } else {
              reject(new Error('获取 Access Token 失败'));
            }
          }
        };
        xhr.send(Object.keys(params).map(function(key) {
          return encodeURIComponent(key) + '=' + encodeURIComponent(params[key]);
        }).join('&'));
      });
    }

    // 点击按钮时开始登录流程
    function login() {
      checkLogin()
        .then(function(access_token) {
          // 如果用户已经登录，则直接使用 Access Token 进行后续操作
          console.log('用户已经登录，Access Token：', access_token);
        })
        .catch(function() {
          // 如果用户未登录，则打开授权页面进行登录
          openAuthPage();
        });
    }

    // 在回调页面中调用该函数以换取 Access Token
    function exchangeCodeForAccessToken(code) {
      getAccessToken(code)
        .then(function(access_token) {
          console.log('获取 Access Token 成功：', access_token);
        })
        .catch(function(err) {
          console.error('获取 Access Token 失败：', err);
        });
    }
  </script>
</body>
</html>
```

### 6 如下是官网的一个例子:[OAuth接入指南 (baidu.com)](https://openauth.baidu.com/doc/doc.html)

## 1. 概述

如果百度用户访问第三方应用网页，则第三方应用可以通过网页授权机制，来获取百度用户基本信息，进而实现自身业务功能。 ![img](https://openauth.baidu.com/doc/assets/img/authorize.1d71cfc8.png)

具体而言，百度帐号网页授权流程分为四步：

1. 引导用户进入授权页面同意授权，获取code；
2. 通过code换取网页授权access_token；
3. 如果需要，开发者可以刷新网页授权access_token，避免过期；
4. 通过网页授权access_token获取用户基本信息。

## [#](https://openauth.baidu.com/doc/doc.html#_2-引导用户完成授权获取code)2. 引导用户完成授权获取code

开发时，需要将用户浏览器重定向到如下URL地址。 

接口调用请求说明：

```text
GET https://openapi.baidu.com/oauth/2.0/authorize?response_type=CODE&client_id=API_KEY&redirect_uri=REDIRECT_URI&scope=SCOPE&state=STATE
```

参数说明：

| **参数名**     | **类型** | **是否必须** | **描述**                                                     |
| :------------- | :------- | :----------- | :----------------------------------------------------------- |
| response_type  | string   | 是           | 固定为 code。                                                |
| client_id      | string   | 是           | 注册应用时获得的API Key。                                    |
| redirect_uri   | string   | 是           | 授权后要回调的URI，即接收Authorization Code的URI。如果用户在授权过程中取消授权，会回调该URI，并在URI末尾附上error=access_denied参数。对于无Web Server的应用，其值可以是“oob”，此时用户同意授权后，授权服务会将Authorization Code直接显示在响应页面的页面中及页面title中。非“oob”值的redirect_uri按照如下规则进行匹配：（1）如果开发者在“授权安全设置”中配置了“授权回调地址”，则redirect_uri必须与“授权回调地址”中的某一个相匹配； （2）如果未配置“授权回调地址”，redirect_uri所在域名必须与开发者注册应用时所提供的网站根域名列表或应用的站点地址（如果根域名列表没填写）的域名相匹配。**授权回调地址配置请参考附录Ⅰ-1**。 |
| scope          | string   | 否           | 以空格分隔的权限列表，若不传递此参数，代表请求用户的默认权限。可填basic或mobile。 |
| display        | string   | 否           | 登录和授权页面的展现样式，默认为“page”，**具体参数定义请参考附录Ⅰ-2**。 |
| state          | string   | 否           | 重定向后会带上state参数。建议开发者利用state参数来防止CSRF攻击。 |
| force_login    | int      | 否           | 如传递“force_login=1”，则加载登录页时强制用户输入用户名和口令，不会从cookie中读取百度用户的登陆状态。 |
| confirm_login  | int      | 否           | 如传递“confirm_login=1”且百度用户已处于登陆状态，会提示是否使用已当前登陆用户对应用授权。 |
| login_type     | string   | 否           | 如传递“login_type=sms”，授权页面会默认使用短信动态密码注册登陆方式。 |
| qrext_clientid | string   | 否           | 网盘扫码透传字段                                             |
| bgurl          | string   | 否           | 二维码登录方式的背景图片url链接，需要encode                  |
| qrcodeW        | int      | 否           | 自定义二维码图片的宽度                                       |
| qrcodeH        | int      | 否           | 自定义二维码图片的高度                                       |
| qrcode         | int      | 否           | 如传递“qrcode=1”，登录授权页面将增加扫码登录入口；**注：扫码登录入口点击跳转至二维码页面，目前支持PC、TV、音箱、watch、kindle** |
| qrloginfrom    | string   | 否           | 扫码登录被扫码端设备类型；目前传参仅支持：pc、tv、speakers、watch、kindle；注：speakers为音箱的标志；**说明：此配置仅支持display=tv时；** |
| userReg        | int      | 否           | 如传递“qrcode=1”，扫码登录页配置“用户名登录”、“注册”入口；**说明：此配置仅支持display=tv时；** |
| appTip         | string   | 否           | 扫码登录页二维码底部提示文案，中文文案需encodeURIComponent('提示文案')；**说明：此配置仅支持display=tv时；** |
| appName        | string   | 否           | 扫码登录页二维码底部app文案配置，中文文案需encodeURIComponent('网盘App')；**说明：此配置仅支持display=tv时；** |

下图为登录授权页面：

![img](https://openauth.baidu.com/doc/assets/img/oauthpage.6f6e552b.png)

无scope权限或redirect_uri不合法时，会展示错误页面，并提示出错原因，如下图示：

![img](https://openauth.baidu.com/doc/assets/img/error1.0518bf45.png)

![img](https://openauth.baidu.com/doc/assets/img/error2.478c6b02.png)

用户同意授权后：页面将跳转至redirect_uri/?code=CODE&state=STATE。 

code说明：code作为换取access_token的票据，每次用户授权带上的code将不一样，code只能使用一次，10分钟未被使用自动过期。

## [#](https://openauth.baidu.com/doc/doc.html#_3-code获取授权access-token)3. code获取授权access_token

redirect_uri指定的开发者服务器地址，在获取到授权code参数后，从服务端向百度开放平台发起如下HTTP请求，通过code换取网页授权access_token。 

注意：access_token长度保留256字符。 

接口调用请求说明：

```text
GET https://openapi.baidu.com/oauth/2.0/token?grant_type=authorization_code&code=CODE&client_id=AP I_KEY&client_secret=SECRET_KEY&redirect_uri=REDIRECT_URI    
```

参数说明：

| **参数名 **    | **类型 ** | **是否必须 ** | **描述 **                                                    |
| :------------- | :-------- | :------------ | :----------------------------------------------------------- |
| grant_type     | string    | 是            | 固定为authorization_code                                     |
| code           | string    | 是            | 用户授权后得到code                                           |
| client_id      | string    | 是            | 应用的API Key                                                |
| client_secret  | string    | 是            | 应用的Secret Key                                             |
| redirect_uri   | string    | 是            | **该值必须与获取Authorization  Code时传递的“redirect_uri”保持一致。** |

返回值说明：

| **字段名 **    | **类型 ** | **描述 **                                                    |
| :------------- | :-------- | :----------------------------------------------------------- |
| access_token   | string    | 获取到的网页授权接口调用凭证                                 |
| expires_in     | int       | Access Token的有效期，以秒为单位                             |
| refresh_token  | string    | 用于刷新Access Token的Refresh Token，所有应用都会返回该参数**（10年的有效期**） |
| scope          | string    | Access Token最终的访问范围，即用户实际授予的权限列表（用户在授权页面时，有可能会取消掉某些请求的权限） |
| session_key    | string    | 基于http调用Open API时所需要的Session Key，其有效期与Access Token一致 |
| session_secret | string    | 基于http调用Open  API时计算参数签名用的签名密钥              |

错误情况下：

| **字段名 **        | **类型 ** | **描述 **                                     |
| :----------------- | :-------- | :-------------------------------------------- |
| error              | string    | 错误码，**关于错误码的详细信息请参考附录Ⅰ-3** |
| error_description  | string    | 错误描述信息，用来帮助理解和解决发生的错误    |

返回值示例：

```text
{  
     "access_token":  "1.a6b7dbd428f731035f771b8d15063f61.86400.1292922000-2346678-124328",  
     "expires_in":  86400,  
     "refresh_token":  "2.385d55f8615fdfd9edb7c4b5ebdc3e39.604800.1293440400-2346678-124328",               
     "scope":  "basic  email",  
     "session_key":  "ANXxSNjwQDugf8615OnqeikRMu2bKaXCdlLxn",  
     "session_secret":  "248APxvxjCZ0VEC43EYrvxqaK4oZExMB"  
} 
```

出错时返回：

```text
{  
     "error":  "invalid_grant",  
     "error_description":  "Invalid  authorization  code:  ANXxSNjwQDugOnqeikRMu2bKaXCdlLxn"   
} 
```

## [#](https://openauth.baidu.com/doc/doc.html#_4-按需刷新access-token)4. 按需刷新access_token

当access_token过期后，可以使用refresh_token进行刷新。refresh_token有效期为十年。 

接口调用请求说明：

```text
GET https://openapi.baidu.com/oauth/2.0/token?grant_type=refresh_token&refresh_token=REFRESH_TOKEN &client_id=API_KEY&client_secret=SECRET_KEY 
```

参数说明：

| **参数名**    | **类型** | **是否必须** | **描述**                                  |
| :------------ | :------- | :----------- | :---------------------------------------- |
| grant_type    | string   | 是           | 固定为refresh_token                       |
| refresh_token | string   | 是           | 通过access_token获取到的refresh_token参数 |
| client_id     | string   | 是           | 应用的API Key                             |
| client_secret | string   | 是           | 应用的Secret Key                          |

返回值说明：

| **字段名 **     | **类型 ** | **描述 **                                                    |
| :-------------- | :-------- | :----------------------------------------------------------- |
| access_token    | string    | 获取到的网页授权接口调用凭证                                 |
| expires_in      | int       | Access Token的有效期，以秒为单位                             |
| refresh_token   | string    | 用于刷新Access Token的Refresh Token，所有应用都会返回该参数（**10年的有效期**） |
| scope           | string    | Access Token最终的访问范围，即用户实际授予的权限列表（用户在授权页面时，有可能会取消掉某些请求的权限） |
| session_key     | string    | 基于http调用OpenAPI时所需要的Session Key，其有效期与 Access Token一致 |
| session_secret  | string    | 基于http调用OpenAPI时计算参数签名用的签名密钥。              |

错误情况下：

| 字段名             | 类型    | 描述                                          |
| :----------------- | :------ | :-------------------------------------------- |
| error              | string  | 错误码，**关于错误码的详细信息请参考附录Ⅰ-3** |
| error_description  | string  | 错误描述信息，用来帮助理解和解决发生的错误    |

返回值示例：

```text
{  
     "access_token":  "1.a6b7dbd428f731035f771b8d15063f61.86400.1292922000-2346678-124328",               
     "expires_in":  86400,  
     "refresh_token":  "2.af3d55f8615fdfd9edb7c4b5ebdc3e32.604800.1293440400-2346678-124328",               
     "scope":  "basic  email",  
     "session_key":  "ANXxSNjwQDugf8615OnqeikRMu2bKaXCdlLxn",  
     "session_secret":  "248APxvxjCZ0VEC43EYrvxqaK4oZExMB"  
} 
```

出错时返回：

```text
{
     "error": "expired_token",
     "error_description": "refresh token has been used"
}
```

## [#](https://openauth.baidu.com/doc/doc.html#_5-获取授权用户信息)5. 获取授权用户信息

获取access_token之后，开发者可以通过access_token拉取用户信息。 

接口调用请求说明：

```text
GET https://openapi.baidu.com/rest/2.0/passport/users/getInfo?access_token=access_token 
```

参数说明：

| **参数名 **   | **类型 ** | **是否必须 ** | 描述                                   |
| :------------ | :-------- | :------------ | :------------------------------------- |
| access_token  | string    | 是            | 由上述步骤获取的OpenAPI接口调用凭证    |
| get_unionid   | int       | 否            | 需要获取unionid时，传递get_unionid = 1 |

返回参数：

| **参数名**     | **参数类型** | **是否必需** | **示例值**                       | **描述**                                                     |
| :------------- | :----------- | :----------- | :------------------------------- | :----------------------------------------------------------- |
| openid         | string       | 是           | oPXyY4O0ZTmUqSX4MRxYDDCccT6Kc9E  | 百度用户的唯一标识，对当前开发者帐号、当前应用唯一           |
| unionid        | string       | 否           | uA91qQ6gAISTuy0mMqoeh7lZ0w6x478  | 百度用户统一标识，对当前开发者帐号唯一                       |
| userid         | uint         | 否           | 67411167                         | 老版 百度用户的唯一标识，后续不在返回该字段                  |
| securemobile   | uint         | 否           | 188888888                        | 当前用户绑定手机号（需要向开放平台申请权限）                 |
| username       | string       | 否           | t***e                            | 当前登录用户的展示用户名，包含打码"*"号                      |
| portrait       | string       | 否           | e2c1776c31393837313031319605     | 当前登录用户的头像，头像地址拼接使用方法：https://himg.bdimg.com/sys/portrait/item/{$portrait} |
| userdetail     | string       | 否           | 喜欢自由                         | 自我简介，可能为空。                                         |
| birthday       | string       | 否           | 1987-01-010000-00-00为未知       | 生日，以yyyy-mm-dd格式显示。                                 |
| marriage       | string       | 否           | 0:未知,1:单身,2:已婚3:恋爱4:离异 | 婚姻状况                                                     |
| sex            | string       | 否           | 0:未知,1:男,2:女                 | 性别                                                         |
| blood          | string       | 否           | 0:未知,1:A,2:B,3:O,4:AB,5:其他   | 血型                                                         |
| is_bind_mobile | uint         | 否           | 0:未绑定,1:已绑定                | 是否绑定手机号                                               |
| is_realname    | uint         | 否           | 0:未实名制,1:已实名制            | 是否实名制                                                   |

错误情况下：

| **字段名 ** | **类型 ** | **描述 **                                  |
| :---------- | :-------- | :----------------------------------------- |
| error_code  | int       | 错误码                                     |
| error_msg   | string    | 错误描述信息,用来帮助理解和解决发生的错误  |

**关于错误码的详细信息请参考附录Ⅰ-5.4** 

返回值示例：

```text
{    
     "openid": "oPXyY4O0ZTmUqSX4MRxYDDCccT6Kc9E",
     "unionid": "uA91qQ6gAISTuy0mMqoeh7lZ0w6x478",
     "userid": "2097322476",
     "username": "u***9",
     "userdetail": "喜欢自由", 
     "birthday": "1987-01-01",
     "marriage": "0",
     "sex": "1",
     "blood": "3",
     "is_bind_mobile": "1",
     "is_realname": "1" 
}
```

出错时返回：

```text
{  
     "error_code": "100",  
     "error_msg": "Invalid parameter"   
```