from suds.client import Client  # 导入suds.client 模块下的Client类

wsdl_url = "http://192.168.0.7:8075/api/01/?wsdl"
#pip install suds-py3

def say_hello_test(url):
    client = Client(url)  # 创建一个webservice接口对象
    client.service.invokeSrv()  # 调用这个接口下的getMobileCodeInfo方法，并传入参数
    req = str(client.last_sent())  # 保存请求报文，因为返回的是一个实例，所以要转换成str
    response = str(client.last_received())  # 保存返回报文，返回的也是一个实例
    print(req)
    print("----------------")
    print(response)



if __name__ == '__main__':
    say_hello_test(wsdl_url)