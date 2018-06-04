from django.shortcuts import render,HttpResponse
from django.urls import reverse
# Create your views here.
def test(request):
    # #反向生成URL,
    # # include导入其他文件路径，include('app01.urls',namespace='aaa')#
    # #app01.urls
    #     #aaa:login
    # #  如果分发的时候指定了include,和namesapce，需要加上namesapce。为了解决name冲突
    # url=reverse("extraapp:login")
    # print(url)
    # return HttpResponse("...")
    # url = reverse("extraapp:app01_userinfo_add")
    # print(url)
    return HttpResponse("...")


def ttt(request):
    url = reverse("tt")
    print(url)
    return HttpResponse("...")