from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    bloglist=Blog.objects
    return render(request,'blog/allblogs.html',{'blogs':bloglist})

def detail(request,blog_id):
    post=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'post':post})