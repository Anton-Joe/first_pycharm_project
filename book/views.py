from django.http import HttpResponse


def book_detail(request, book_id, category_id):
    # 可以从数据库中根据Book_id提取这个图书的信息
    text = "您获取的图书id是{id}，分类id是{id2}".format(id=book_id, id2=category_id)
    return HttpResponse(text)


def author_detail(request):
    author_id = request.GET['id']
    text = "作者的id是{id}".format(id=author_id)
    return HttpResponse(text)


def publisher_detail(request, publisher_id):
    text = "出版社的id是{id}".format(id=publisher_id)
    return HttpResponse(text)


def book(request):
    return HttpResponse('图书')


def book_list(request):
    return HttpResponse('图书列表')
