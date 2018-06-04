# #!/usr/bin/env python
# #encoding:utf-8
# class Foo():
#
#
#     def get_urls(self):
#         # print(self.add)
#         # print(self.delete)
#         ret=[self.add,self.delete]
#         return ret
#
#     @property
#     def urls(self):
#         return self.get_urls()
#
#
#     def add(self):
#        return "add"
#
#     def delete(self):
#         return "delete"
#
# f=Foo()
# for i in f.urls:
#     print(i())

#单例模式
#方法1 模块导入
# site=ExtraAppSite()

#方法2类方法
# class Foo():
#     _instance=None
#     def __init__(self):
#         pass
#     @classmethod
#     def get_instance(cls):
#         if cls._instance:
#             return cls._instance
#         else:
#             obj=cls()
#             cls._instance=obj
#             return obj
# a1=Foo.get_instance()

#方法3__new__
# class Foo():
#     _instance=None
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs): #创建对象
#         if cls._instance:
#             return cls._instance
#         else:
#             obj=object.__new__(cls, *args, **kwargs) #创建出来的对象传给init self里面
#             cls._instance=obj
#         return obj
#
#  #用户行为不需要改变
# obj=Foo()
# obj1=Foo()
# print(obj)
# print(obj1)

#单例模式的用处
    # 自定义CURD组件时，没有必要创建多个实例来浪费空间
    # 发布文章，对于特殊字符的过滤KindEditor
        # class Kind():
        #     def __init__(self):
        #         self.valid_tags=[
        #             "a","div","h1"
        #         ]
        #     def valid(self,content):
        #         pass
        # obj=Kind()
        # body=obj.valid("<html>")
