from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # 2. 使用 render 函数
    # render(request对象, 模板路径, 上下文数据字典)
    return render(request, 'rango/index.html', context=context_dict)

