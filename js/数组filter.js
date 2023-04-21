let cities = [{
        name: 'Los Angeles',
        population: 3792621
    },
    {
        name: 'New York',
        population: 8175133
    },
    {
        name: 'Chicago',
        population: 2695598
    },
    {
        name: 'Houston',
        population: 2099451
    },
    {
        name: 'Philadelphia',
        population: 1526006
    }
];
//如下是自己写的实现
let bigCities = [];
for (let i = 0; i < cities.length; i++) {
    if (cities[i].population > 3000000) {
        bigCities.push(cities[i]);
    }
}

cities.forEach(item => {
    console.log(item)
})
abc = []
cities.forEach(function fn(item) {
    if (item.population > 3000000) {
        abc.push(item)
    }
})
console.log("==========================================")
// console.log(bigCities);
console.log(abc)
console.log("==========================================")

//使用数组的filter
let a = cities.filter(item => item.name.match("New"))
console.log(a)