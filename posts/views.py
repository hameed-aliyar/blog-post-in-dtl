from django.shortcuts import redirect, render

from posts.forms import CreatePostForm, EditPostForm, LoginForm, RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Posts, Profile

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
            post = form.save(commit=False)
            post.author = request.user  # ✅ Set the author here
            post.save()
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
    
def loginn(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            try:
                profile = Profile.objects.get(email=email)
                user = profile.user
            except Profile.DoesNotExist:
                return render(request, "posts/login.html", {'form': form, 'error': 'Invalid email or password.'})
            if user.check_password(password):
                login(request, user)
                return redirect("posts-home")
            else:
                return render(request, "posts/login.html", {'form': form, 'error': 'Invalid email or password.'})
    form = LoginForm()
    return render(request, "posts/login.html", {'form': form} )

def logoutt(request):
    logout(request)
    return redirect("posts-home")

def myposts(request):
    posts = Posts.objects.filter(author=request.user)
    return render(request, "posts/myposts.html", {'posts': posts})