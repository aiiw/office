// setTimeout(function () {
//     console.log("First");
//     setTimeout(function () {
//         console.log("Second");
//         setTimeout(function () {
//             console.log("Third");
//         }, 3000);
//     }, 2000);
// }, 1000);

function SetTime(t, content) {
    return new Promise((a, b) => {
        setTimeout(() => {
            a(content)
        }, t)
    })
}

(() => {
    SetTime(1000, 'First').then(data => {
        console.log('1', data);

        return new Promise((a, b) => {
            setTimeout(() => {
                a('Second')
            }, 2000);
        })



    }).then((data) => {
        console.log('2', data);

        return new Promise((a, b) => {
            setTimeout(() => {
                a('Third')
            }, 3000);
        })



    }).then((data) => {
        console.log('3', data);
    })
})()