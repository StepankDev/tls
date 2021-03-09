from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from . models import *

def index(request):
    posts = BlogPost.objects.order_by('-date_published').filter(is_published=True)
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'posts': paged_posts
    }
    
    return render(request, 'pages/blog.html', context)

def post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'pages/post.html', context) 
