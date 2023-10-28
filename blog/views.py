from django.http import HttpResponse
from django.shortcuts import render ,redirect
from blog.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages
import random  # Import the random module

def home(request):
    # Get all posts
    all_posts = Post.objects.all()
    
    # Shuffle the posts randomly
    random_posts = list(all_posts)
    random.shuffle(random_posts)
    
    # Get the first 11 random posts
    posts = random_posts[:11]

    # Get all categories
    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cats = Category.objects.all()
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "home.html", {'cat': cat, 'posts': posts, 'cats': cats})

def contact(request):
    cats = Category.objects.all()
    if request.method=="POST":
        name =request.POST.get("name")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        feedback=request.POST.get("feedback")
        my_feedback=Feedback(name=name, email=email, mobile=mobile , feedback=feedback)
        my_feedback.save()
        messages.success(request,"Your message has been sent!")
    return render(request, 'contact.html',{'cats': cats})


def about(request):
    cats = Category.objects.all()
    return render(request, 'about.html',{'cats': cats})

def logoutUser(request):
    logout(request)
    messages.success(request,"Logout successfully!")
    return redirect("/")

def loginUser(request):
    if request.method=="POST":
        username =request.POST.get("username")
        password=request.POST.get("password")
        print (username , password) 
        user = authenticate(username = username ,password=password)
        if user is not None:
            login(request ,user)
            messages.success(request,"Login successfully!")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentials, Please try again!")
            return render(request, 'login.html')
    return render(request, 'login.html')


def regi(request):
    if request.method=="POST":
        username =request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        print (username, email , password)
        my_user=User.objects.create_user(username, email, password)
        my_user.save()
        messages.success(request,"Register successfully!")
        return redirect("/login")
    return render(request, 'regi.html')




    #project
def show_project_page(request):
    languages=Language.objects.all()
    projects=Project.objects.all()
    return render(request, "projectHome.html", {'projects': projects, 'languages': languages})
    
def projectPost(request, title):
    projects = Project.objects.get(title=title)
    languages = Language.objects.all()
    return render(request, 'projectPost.html', {'projects': projects, 'languages': languages})

def show_language_page(request,cid):
    languages=Language.objects.all()
    language_c=Language.objects.get(pk=cid)
    projects=Project.objects.filter(language=language_c)
    return render(request, "projectHome.html", {'projects': projects, 'languages': languages})

def projectSearch(request):
    query=request.GET['query']
    print(query)
    allpost =Project.objects.filter(title__icontains=query)
    gh=Project.objects.filter(content__icontains=query)
    return render(request,'projectSearch.html',{'allpost':allpost,'gh':gh})

def search(request):
    cats = Category.objects.all()
    query=request.GET['query']
    print(query)
    allpost =Post.objects.filter(title__icontains=query)
    gh=Post.objects.filter(content__icontains=query)
    return render(request,'search.html',{'allpost':allpost,'gh':gh,'cats': cats})