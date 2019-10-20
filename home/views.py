from django.shortcuts import render,get_object_or_404
from blog.models import Blog

def homepage(request):
    bloglist = Blog.objects
    return render(request,'home/home.html',{'blogs':bloglist})