![image-20240527094004054](https://gitee.com/aiiw/images/raw/master/img/image-20240527094004054.png)

附加例子:

```
from functools import wraps
def logit(func):
	@wraps(func)
	def with_logging(*args, **kwargs):
		print(func.__name__ + " was called")
		return func(*args, **kwargs)
	return with_logging
@logit
def addition_func(x):
	"""Do some math."""
	return x + x
result = addition_func(4)
print(result)
# Output: addition_func was called



def logit1(func):
	def with_logging1(x):
		def with_logging2(*args, **kwargs):
			print(func.__name__ + " was called","看看这个x是多少",x)
			return func(*args, **kwargs)
		return with_logging2
	return with_logging1
def addition_func1(x):

	return x

logit1(addition_func1)(100)(2)


@logit1(1)
def aiiw():
	pass;
```

