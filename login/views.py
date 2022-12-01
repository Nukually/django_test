from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import models

# Create your views here.

user_list = []


def index(request):
    # return HttpResponse("hello,world")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        models.UserInfo.objects.create(user=username, pwd=password)
        # print(username, password)
    user_list = models.UserInfo.objects.all()
    print(user_list)
    return render(request, 'index.html', {'data': user_list})
