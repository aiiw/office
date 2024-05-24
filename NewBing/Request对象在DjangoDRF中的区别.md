假设您有一个POST请求，请求体是一个JSON格式的数据，如{“name”: “Alice”, “age”: 25}。

如果您使用django的request对象，您可以通过request.body来获取请求体的原始字节数据，如b’{“name”: “Alice”, “age”: 25}'。然后您需要自己解析这个字节数据为Python对象，如json.loads(request.body)。

如果您使用DRF的request对象，您可以直接通过request.data来获取请求体的已解析的Python对象，如{“name”: “Alice”, “age”: 25}。DRF会根据请求头中的Content-Type字段来自动解析不同格式的数据，如JSON、XML、Form等。

另外，如果您有一个GET请求，请求URL是http://example.com/api/users?name=Alice&age=25。

如果您使用django的request对象，您可以通过request.GET来获取查询参数的QueryDict对象，如<QueryDict: {‘name’: [‘Alice’], ‘age’: [‘25’]}>。然后您需要自己处理这个QueryDict对象中的多值键或列表值等情况。

如果您使用DRF的request对象，您可以通过request.query_params来获取查询参数的QueryDict对象，并且DRF会提供一些额外的方法和属性来方便地处理多值键或列表值等情况。