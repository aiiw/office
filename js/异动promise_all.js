function a() {
    return new Promise((reslove) => {
        setTimeout(() => {
            reslove(123)
        }, 10000)

    })
}

function b() {
    return new Promise((reslove) => {
        setTimeout(() => {
            reslove(123)
        }, 10000)

    })
}

async function bb() {
    let qq = await Promise.all([a(), b()])
    console.log(qq);


}

bb()