from django.shortcuts import render #shorter version
from django.http import HttpResponse
from .models import Post
# Create your views here.


def home(request):
    posts=Post.objects.all()

    context={'posts': posts}
    return render(request,'blog/home.html',context=context)

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})

