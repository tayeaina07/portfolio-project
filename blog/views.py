from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblog(request):
    blog = Blog.objects
    return render(request, 'blog/allblog.html', {'blog':blog})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})
