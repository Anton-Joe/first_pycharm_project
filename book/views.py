from django.http import HttpResponse


def book(request):
    return HttpResponse('图书')


def book_detail(request, book_id):
    # 可以从数据库中根据Book_id提取这个图书的信息
    text = "您获取的图书id是{id}".format(id=book_id)
    return HttpResponse(text)
