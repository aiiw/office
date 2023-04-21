// function a(b) {
//     b();
//     console.log("aaa");
// }

// function b() {
//     console.log("bbbb");
// }

// a(b);
// // bbbb
// // aaa

async function a(b) {
    await b();
    console.log("aaa");
}

async function b() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("bbb");
            resolve();
        }, 3000);
    });
}

a(b);

// bbb
// aaa