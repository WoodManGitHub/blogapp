from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils.html import strip_tags
import markdown

def index(request):
	post_list = Post.objects.all().order_by('-created_time')
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
