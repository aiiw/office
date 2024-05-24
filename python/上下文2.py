# _*_ coding:utf-8 _*_

from contextlib import contextmanager

@contextmanager
def book_mark():
    print('《sss', end="")
    yield
    print('》', end="")

with book_mark():
    # 核心代码
    print('且将生活一饮而尽', end="")