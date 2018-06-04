#!/usr/bin/env python
#encoding:utf-8

from django.shortcuts import HttpResponse,render,redirect
from django.urls import reverse
from django.http.request import QueryDict
class BaseExtraAdmin(object):
    list_display="__all__"
    add_or_edit_model_form=None

    def __init__(self,model_class,site):
        self.model_class=model_class
        self.site=site
        self.request=None
        self.app_label=model_class._meta.app_label
        self.model_name=model_class._meta.model_name

    def get_add_or_edit_model_form(self):
        if self.add_or_edit_model_form:
            return self.add_or_edit_model_form
        else:
            #对象由类创建，类由type创建
            from django.forms import ModelForm
            # class MyModelForm(ModelForm):
            #     class Meta:
            #         model = self.model_class
            #         fields = "__all__"
            # return MyModelForm
            _m=type('Meta',(object,),{'model':self.model_class,'fields':'__all__'})
            MyModelForm=type('MyModelForm',(ModelForm,),{'Meta':_m})
            return MyModelForm

    @property
    def urls(self):
        from django.conf.urls import url, include
        info=self.model_class._meta.app_label,self.model_class._meta.model_name
        urlpatterns = [
            url(r'^$', self.changelist_view, name='%s_%s_changelist' % info),
            url(r'^add/$', self.add_view, name='%s_%s_add' % info),
            url(r'^(.+)/delete/$', self.delete_view, name='%s_%s_delete' % info),
            url(r'^(.+)/change/$', self.change_view, name='%s_%s_change' % info),
            # url(r'^(.+)/detail/$', self.detail_view, name='%s_%s_detail' % info),
            # For backwards compatibility (was the change url before 1.9)
            # url(r'^(.+)/$', RedirectView.as_view(pattern_name='%s:%s_%s_change' % ((self.backend_site.name,) + info))),
        ]
        return urlpatterns

    def changelist_view(self,request):
        """
        查看列表
        :param requset:
        :return:
        """
        #生成页面上的添加按钮
        #namespace，app_label,model_name

        # print(request.GET.urlencode()) #urlencode获取url
        param_dict=QueryDict(mutable=True) #设置为可修改
        if request.GET:
            param_dict['_changlistfilter']=request.GET.urlencode()
        base_add_url = reverse("{2}:{0}_{1}_add".format(self.app_label, self.model_name, self.site.namespace))
        add_url="{0}?{1}".format(base_add_url,param_dict.urlencode())


        self.request=request
        result_list=self.model_class.objects.all()
        #前端要显示下面的内容，要扩展simple_tag
        # print(result_list)
        # print(self.list_display)

        context={
            'result_list':result_list,
            'list_display':self.list_display,
            'BaseExtraAdmin_obj':self,
            'add_url':add_url

        }
        return render(request, 'exapp/change_list.html',
                      # {'result_list':result_list,'list_display':self.list_display}
                        context #同上一样
                      )

    def add_view(self,request):
        """
        添加数据
        :param request:
        :return:
        """
        if request.method=="GET":
            print(request.GET.get("_changlistfilter"))
            model_form_obj=self.get_add_or_edit_model_form()()
        else:
            model_form_obj = self.get_add_or_edit_model_form()(data=request.POST,files=request.FILES)
            if model_form_obj.is_valid():
                model_form_obj.save()
                #添加成功进行跳转
                base_list_url = reverse(
                    "{2}:{0}_{1}_changelist".format(self.app_label, self.model_name, self.site.namespace))
                list_url = "{0}?{1}".format(base_list_url, request.GET.get("_changlistfilter"))
                return redirect(list_url)

        context={
            'form':model_form_obj
        }
        return render(request,'exapp/add.html',context)


    def delete_view(self,request,pk):
        """
        删除数据
        :param request:
        :param pk:
        :return:
        """
        """
        根据pk获取数据，然后delete()
        获取url，跳转回列表页面
        """

        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        data = "%s_%s_delete" % info
        return HttpResponse(data)

    def change_view(self,request,pk):
        """
        修改数据
        :param request:
        :param pk:
        :return:
        """
        #1、获取_changelistfilter中传递的参数
        #request.GET.get("_changlistfilter")
        #2、页面显示并提供默认值ModelForm
        obj=self.model_class.objects.filter(pk=pk).first()
        if not obj:
            return HttpResponse("id不存在")
        if request.method=="GET":
            model_form_obj=self.get_add_or_edit_model_form()(instance=obj)
        else:
            model_form_obj = self.get_add_or_edit_model_form()(data=request.POST,files=request.FILES,instance=obj) #成功
            if model_form_obj.is_valid():
                model_form_obj.save()
            base_list_url = reverse(
                "{2}:{0}_{1}_changelist".format(self.app_label, self.model_name, self.site.namespace))
            list_url = "{0}?{1}".format(base_list_url, request.GET.get("_changlistfilter"))
            return redirect(list_url)
        # 3、返回页面
        context={
            'form':model_form_obj
        }

        return render(request,'exapp/edit.html',context)




    # def detail_view(self,request):
    #     """
    #     详情
    #     :param request:
    #     :return:
    #     """
    #     info = self.model_class._meta.app_label, self.model_class._meta.model_name
    #     data = "%s_%s_detail" % info
    #     return HttpResponse(data)


class ExtraAppSite(object):
    def __init__(self):
        self._registry={}
        self.namespace="extraapp"
        self.app_name="extraapp"

    def register(self,model_class,xxx=BaseExtraAdmin):
        self._registry[model_class]=xxx(model_class,self)
        """
        {
            UserInfo类:BaseExtraAdmin(UserInfo类,ExtraAppSite对象) ExtraAppUserInfo对象,
            Role类:BaseExtraAdmin(Role类,ExtraAppSite对象)
            XX类:BaseExtraAdmin(XX类,ExtraAppSite对象)
        }
        """

    def get_urls(self):
        from django.conf.urls import url, include
        ret=[
            url(r'^login/',self.login,name='login'),
            url(r'^logout/',self.logout,name='logout')
        ]
        for model_cls,extraapp_admin_obj in self._registry.items():
            app_label=model_cls._meta.app_label
            model_name=model_cls._meta.model_name
            # print(extraapp_admin_obj)
            #<class 'app01.models.Role'> app01 role
            # print(model_cls,app_label,model_name)
            ret.append(url(r'^%s/%s/'%(app_label,model_name), include(extraapp_admin_obj.urls)))
        return ret

    @property
    def urls(self):
        return (self.get_urls(),self.app_name,self.namespace)

    def login(self,request):
        return HttpResponse("login")

    def logout(self,request):
        return HttpResponse("logout")


site=ExtraAppSite()