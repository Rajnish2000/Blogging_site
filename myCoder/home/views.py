from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
# Create your views here.

def index(request):
    post = Post.objects.all()
    print(post)
    return render(request, 'home/index.html', {'posts': post})


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        if len(name) < 3 or len(email) < 4 or len(phone) < 10 or len(message) < 6:
            messages.error(
                request, 'please enter the contact form correctly !')
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, message=message)
            contact.save()
            messages.success(
                request, 'your contact form has been submitted successfully !')

    return render(request, 'home/contact.html')


def search(request):
    query = request.GET['query']
    # post = Post.objects.all()
    if len(query) > 150 or len(query) == 0:
        # post = []
        post = Post.objects.none()
        messages.warning(
            request, 'No search result are available the given query | Please refine your query !')
    else:
        postTitle = Post.objects.filter(title__icontains=query)
        postContent = Post.objects.filter(content__icontains=query)
        postAuthor = Post.objects.filter(author__icontains=query)
        post = postTitle.union(postContent, postAuthor)
    # if post.count() == 0:
    return render(request, 'home/search.html', {'posts': post, 'query': query})


def handleSignUp(request):
    if request.method == 'POST':
        # print(request)
        # get the post parameter
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        # check for errorneous inputs
        if len(username) > 10:
            messages.error(
                request, 'username must be greater then 10 character ')
            return redirect('home')
        if not username.isalnum():
            messages.error(request, 'username must be alphnumric character ')
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, 'pass1 and are not matched ')
            return redirect('home')

        # create User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, 'your account has been successfully created !')
        return redirect('/')

    else:
        return HttpResponse('404 -- not Found !')


def handleLogin(request):
    if request.method == 'POST':
        # get the post parameter
        loginUsername = request.POST['logUsername']
        loginPassword = request.POST['logPassword']
        user = authenticate(username=loginUsername, password=loginPassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Log in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid user / please try again')
            return redirect('/')

    return HttpResponse('404-- not found ')


def handleLogout(request):

    logout(request)
    messages.success(request, 'Successfully log Out')
    return redirect('/')

    return HttpResponse('log Out')


def profile(request):
    # user = authenticate(username=loginUsername, password=loginPassword)
    # profile = User.objects.filter(profile__activation_key=user).exists()
    # print(User)
    return render(request,'home/profile.html')
                                          






# username :  Rajnish2000
# 71430442+Rajnish2000@users.noreply.github.com