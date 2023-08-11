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


# class MyResource:
#     def query(self):
#         print("query data")

# @contextmanager
# def make_myresource():
#     print("connect to resource")
#     yield MyResource()
#     print("connect to resource")

# with make_myresource() as r:
#     r.query()


# from contextlib import contextmanager

# @contextmanager
# def make_open_context(filename, mode):
#     fp = open(filename, mode)
#     try:
#         yield fp
#     finally:
#         fp.close()

# with make_open_context('a.txt', 'a') as file_obj:
#     file_obj.write("hello carson666")