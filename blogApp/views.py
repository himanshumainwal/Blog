from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blog
from .forms import Edit_Blog

# Create your views here.

def home(request):
    blog = Blog.objects.all()
    context = {'blogs' : blog}
    return render(request, 'home.html', context)

def user_logIn(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')  
       user = authenticate(request, username=username, password=password)
       if user is not None:
            login(request, user)
            return redirect('/')
       else:
            messages.warning(request, 'Email address and Password do not match, try again!')
            return redirect('login')
    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        fName = request.POST.get('fullName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeatPassword = request.POST.get('repeatPassword')
        if password == repeatPassword:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username is already taken')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email is already taken')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Congratulatons! You successfully Registered')
                return redirect('login')
        else:
            messages.warning(request, 'Passwords do not match')   
    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def add_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('des')
        blog = Blog(title=title, des=desc, user_id=request.user)
        blog.save()
        messages.success(request, 'Post has been submitted Successfully')
        return redirect('addBlog')
    return render(request, 'addBlog.html')

def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    context = {'blog' : blog}
    return render(request, 'blogDetail.html', context)

def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request, 'Post has been Deleted')
    return redirect('/')

def edit(request, id):
    blog = Blog.objects.get(id=id)
    editBlog = Edit_Blog(instance=blog)
    if request.method == 'POST':
        form = Edit_Blog(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post has been updated ')
            return redirect('home')
    return render(request, 'editBlog.html', {'editBlog':editBlog})