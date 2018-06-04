#!/usr/bin/env python
#encoding:utf-8
class Foo():


    def get_urls(self):
        # print(self.add)
        # print(self.delete)
        ret=[self.add,self.delete]
        return ret

    @property
    def urls(self):
        return self.get_urls()


    def add(self):
       return "add"

    def delete(self):
        return "delete"

f=Foo()
for i in f.urls:
    print(i())