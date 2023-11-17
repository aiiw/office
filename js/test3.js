const fs = require("fs");

function readDirectory(path) {
    fs.readdir(path, (err, files) => {
        if (err) {
            console.error("读取目录出错：", err);
            return;
        }

        files.forEach(file => {
            console.log("文件或目录：", file);
        });
    });
}

// 读取指定目录的信息
const path = 'C:\\Users\\11608\\Desktop\\public\\gp';
// const directoryPath = "C:\Users\11608\Desktop\public\gp";
readDirectory(path);