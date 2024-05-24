const XLSX = require('xlsx');

// 读取 Excel 文件
const workbook = XLSX.readFile('C:\\Users\\11608\\Desktop\\jzg.xlsx');

// 获取工作表名称
const sheetName = workbook.SheetNames[0];

// 通过工作表名称获取工作表对象
const worksheet = workbook.Sheets[sheetName];

// 将工作表数据解析为 JSON 格式
const jsonData = XLSX.utils.sheet_to_json(worksheet, {
    header: 1
});

// 输出解析后的 Excel 数据
console.log(jsonData);