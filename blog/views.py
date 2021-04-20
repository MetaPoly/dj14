from django.shortcuts import render
from .models import Blog
from django.http import HttpResponseRedirect
# Create your views here.
def allblogs(request):
    blogs=Blog.objects.all
    return render(request,"blog/allblog.html",{"blogs":blogs})
def home(request):
    return HttpResponseRedirect("/static/index.html")