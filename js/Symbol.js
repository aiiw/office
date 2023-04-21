const MY_KEY = Symbol();
let obj = {};
obj[MY_KEY] = 123;
console.log(obj[MY_KEY]); // 123

let obj2 = {
    [MY_KEY]: 123
};
console.log(obj2[MY_KEY]); // 123

let obj3 = {
    [MY_KEY]() {
        return 'bar';
    }
};
console.log(obj3[MY_KEY]()); // bar

log.levels = {
    DEBUG: Symbol('debug'),
    INFO: Symbol('info'),
    WARN: Symbol('warn'),
};

function log(type, message) {
    switch (type) {
        case log.levels.DEBUG:
            console.log(message);
            break;
        case log.levels.INFO:
            console.log(message);
            break;
        case log.levels.WARN:
            console.log(message);
            break;
        default:
            console.log("default");
            break;
    }
}

log(log.levels.DEBUG, 'debug message');
log(log.levels.INFO, 'info message');


const MY_KEY1 = Symbol();
let obj21 = {
    [MY_KEY]: 123,
    enum: 2,
    nonEnum: 3
};

// 获取属性名称的几种方法
console.log(Object.getOwnPropertyNames(obj21)); // ['enum', 'nonEnum']
console.log(Object.getOwnPropertySymbols(obj21)); // [Symbol()]
console.log(Reflect.ownKeys(obj21)); // ['enum', 'nonEnum', Symbol()]