class newobj {
    static PENING = "待定";
    static FULLING = "成功";
    static REJECTED = "失败";

    constructor(fun) {
        this.aiiw = "这个用来测试使用！" //这个地方的变量是可以定义 
        this.status = newobj.PENING
        this.result = ""
        fun(this.a.bind(this), this.b.bind(this)) //这个地方的变量是实参，要提前定义,使用bind可以将this a，放入 constructo{}对像中，使用这个对象的成员变量。
    }
    a1 = "test"
    a(jg) {
        if (this.status === newobj.PENING) {
            this.status = newobj.FULLING
            // console.log("我成功了");
            this.result = jg;
        }

    }
    b(jg) {
        if (this.status === newobj.PENING) {
            this.status = newobj.REJECTED
        }
        // console.log("我失败了");
        this.result = jg;
    }
    then(oncg, onsb) {
        if (this.status === newobj.FULLING) {
            setTimeout(() => {
                oncg(this.result)
            })

        }
        if (this.status === newobj.REJECTED) {
            setTimeout(() => {
                onsb(this.result)
            })
        }
    }

}
console.log("第一步");
//如下这一步已经调试成功
// const myobj = new newobj((resolve, reject) => {
//     console.log("第二步");
//     resolve("这是第X步咯")

// })

// myobj.then((b) => {
//     console.log(b); //其实在这里一定要理解好，有时候有回调函数，已经执行了，并且已经传递了实际参数，例如上面的this.result.然后再让你写形参。
// })
// console.log("第三步");


const myobj1 = new newobj((resolve, reject) => {
    console.log("第二步");
    setTimeout(() => {
        resolve("这是第X步咯"), console.log("这个位置是函数参数");
    })
    console.log("第三步")
}) //这里未解决，没有显示"这是第X步咯"