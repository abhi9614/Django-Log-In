from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


def about(request):
    context = {'posts': 'author'}
    return render(request, 'blog/about.html', context)
