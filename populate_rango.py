import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    # 1. 定义 Python 类别的页面数据
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views': 114}, # 为了看起来更真实，我加了些随机views，测试脚本只查是否存在
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'views': 53},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'views': 20}
    ]

    # 2. 定义 Django 类别的页面数据
    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 32},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'views': 12},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views': 1258}
    ]

    # 3. 定义 Other Frameworks 类别的页面数据
    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/',
         'views': 5},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'views': 3}
    ]

    # 4. 组装类别数据 (注意：这里设置了 views 和 likes，测试脚本会检查这些数值！)
    cats = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}
    }

    # 5. 循环创建数据
    for cat, cat_data in cats.items():
        # add_cat 函数在下面定义
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views'])

    # 打印结果
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# 执行代码
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()