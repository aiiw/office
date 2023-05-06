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

