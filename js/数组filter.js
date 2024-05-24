let cities = [{
        name: 'Los Angeles',
        population: 1
    },
    {
        name: 'New York',
        population: 2
    },
    {
        name: 'Chicago',
        population: 3
    },
    {
        name: 'Houston',
        population: 4
    },
    {
        name: 'Philadelphia',
        population: 5
    }
];
//如下是自己写的实现
let bigCities = [];
for (let i = 0; i < cities.length; i++) {
    if (cities[i].population > 3) {
        bigCities.push(cities[i]);
    }
}

bigCities.forEach(item => {
    console.log('aiiw', item)
})
abc = []
cities.forEach(function fn(item) {
    if (item.population > 3) {
        abc.push(item)
    }
})
console.log("==========================================")
// console.log(bigCities);
console.log(abc)
console.log("==========================================")

//使用数组的filter
let a = cities.filter(item => item.name.match("New")) //这个才是类型列表的推导式,不过它只能过滤.
//match()方法是JavaScript中字符串对象的方法之一，它可以用来在一个字符串中查找匹配的子串，并返回一个包含匹配结果的数组。
console.log(a)