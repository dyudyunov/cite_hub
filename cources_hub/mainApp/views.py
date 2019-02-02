from django.shortcuts import render
from .models import Post
# Create your views here.

def mainPage(request):
    posts = Post.objects.filter(city='online')
    return render(request, 'mainApp\mainPage.html', context={'posts':posts})

def kyiv(request):
    posts = Post.objects.filter(city='kyiv')
    return render(request, 'mainApp\mainPage.html', context={'posts':posts})

def dnipro(request):
    posts = Post.objects.filter(city='dnipro')
    return render(request, 'mainApp\mainPage.html', context={'posts':posts})

def lviv(request):
    posts = Post.objects.filter(city='lviv')
    return render(request, 'mainApp\mainPage.html', context={'posts':posts})

def kharkiv(request):
    posts = Post.objects.filter(city='kharkiv')
    return render(request, 'mainApp\mainPage.html', context={'posts':posts})

def odessa(request):
    posts = Post.objects.filter(city='odessa')
    return render(request, 'mainApp\mainPage.html', context={'posts':posts})
    
def eventdetail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'mainApp\eventdetail.html', context={'post':post})