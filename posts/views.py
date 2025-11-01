from django.shortcuts import redirect, render

from posts.forms import CreatePostForm, EditPostForm, LoginForm, RegisterForm

from django.contrib.auth.models import User
from .models import Posts

# Create your views here.
def home(request):
    posts = Posts.objects.all().order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'posts/home.html', context=context)

def detail(request, pk):
    post = Posts.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, 'posts/detail.html', context=context)

def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts-home')
    else:
        form = CreatePostForm()
    return render(request, 'posts/create.html', {'form': form})

def edit(request, pk):
    post = Posts.objects.get(id=pk)
    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts-home')
    else:
        form = EditPostForm(instance=post)
    return render(request, 'posts/edit.html', {'form': form})

def delete(request, pk):
    post = Posts.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts-home')
    return render(request, 'posts/delete.html', {'post': post})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = f"user_{User.objects.count() + 1}"
            user.save()
            form.save(commit=True)
        return redirect("login")
    form = RegisterForm()
    return render(request, "posts/register.html", {'form': form} )
    
def login(request):
    form = LoginForm()
    return render(request, "posts/login.html", {'form': form} )