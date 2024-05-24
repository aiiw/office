const http = require('http');

const server = http.createServer((req, res) => {
    if (req.method === 'POST' && req.url === '/submit-hardware-info') {
        let data = '';

        req.on('data', chunk => {
            data += chunk;
        });

        req.on('end', () => {
            const hardwareInfo = JSON.parse(data);

            // 在这里对客户端的硬件信息进行处理
            // 例如，生成硬件报告或执行其他操作

            // 返回响应给客户端
            res.setHeader('Content-Type', 'application/json');
            res.end(JSON.stringify({
                message: '成功接收客户端硬件信息'
            }));
        });
    } else {
        res.statusCode = 404;
        res.end();
    }
});

server.listen(3000, () => {
    console.log('服务器已启动，监听端口3000');
});