//12. `map()`: 对每个元素执行函数并返回新数组
// forEach() 方法没有返回值， 它只是遍历数组并对每个元素执行指定的回调函数。
// map() 方法返回一个新数组， 该数组由原始数组中的每个元素经过回调函数处理后的结果组成。
// const numbers14 = [1, 2, 3];
// numbers14.forEach(number => {
//     console.log(number); // 依次输出 1, 2, 3
// });

arr = [{
        value: 'vue',
        link: 'https://github.com/vuejs/vue'
    },
    {
        value: 'element',
        link: 'https://github.com/ElemeFE/element'
    },
    {
        value: 'cooking',
        link: 'https://github.com/ElemeFE/cooking'
    },
    {
        value: 'mint-ui',
        link: 'https://github.com/ElemeFE/mint-ui'
    },
    {
        value: 'vuex',
        link: 'https://github.com/vuejs/vuex'
    },
    {
        value: 'vue-router',
        link: 'https://github.com/vuejs/vue-router'
    },
    {
        value: 'babel',
        link: 'https://github.com/babel/babel'
    },
]

console.log('这个是原始', arr.filter((item) => {
    return item.value == 'babel'
}));

const fun1 = (str) => {
    return (item) => item.value.toLowerCase().indexOf(str.toLowerCase()) === 0
}



console.log('这个是改写', arr.filter(fun1('v')));


console.log("=======================================");


var queryString = 'v'
const createFilter = (queryString) => {
    return (item) => {
        // console.log("正常这个地方也会打印出来的");//对
        return (
            item.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
        )
    }
}

const results = queryString ?
    arr.filter(createFilter(queryString)) : restaurants.value;





console.log(results);