from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils.html import strip_tags
import markdown

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'post_list': post_list})

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blogapp/index.html', context={'post_list': post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blogapp/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.content = markdown.markdown(strip_tags(post.content),
				extensions=[
					'markdown.extensions.extra',
					'markdown.extensions.codehilite',
        				'markdown.extensions.toc',
				], safe_mode=True)
    return render(request, 'blogapp/detail.html', context={'post': post})
