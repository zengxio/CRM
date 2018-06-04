#!/usr/bin/env python
#encoding:utf-8
from django.template import Library
from types import FunctionType
register=Library()


def table_body(result_list,list_display,BaseExtraAdmin_obj):



    #根据字段名获取数据
    for row in result_list:
        if list_display=="__all__":
            yield [str(row),]
        else:
            yield [name(BaseExtraAdmin_obj,obj=row) if isinstance(name,FunctionType) else getattr(row,name) for name in list_display]

def table_head(result_list,list_display,BaseExtraAdmin_obj):
    if list_display == "__all__":
        yield "对象列表"
    else:
        for item in list_display:
            if isinstance(item,FunctionType):
                #运行函数
                yield item(BaseExtraAdmin_obj, is_header=True)
            else:
                #显示中文
                yield BaseExtraAdmin_obj.model_class._meta.get_field(item).verbose_name

        # return [item(BaseExtraAdmin_obj,is_header=True) if isinstance(item,FunctionType) else BaseExtraAdmin_obj.model_class._meta.get_field(item).verbose_name for item in list_display]

# @register.simple_tag #直接把结果传给change_list.html
@register.inclusion_tag("exapp/md.html")  #把值给md.html模版文件，将结果返回给change_list.html
def func(result_list,list_display,BaseExtraAdmin_obj):

    v=table_body(result_list,list_display,BaseExtraAdmin_obj)
    thead=table_head(result_list,list_display,BaseExtraAdmin_obj)
    return {'xxx':v,'table_head':thead}