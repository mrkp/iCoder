from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Contact
from blog.models import Post
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<10:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(
                name = name,
                email = email,
                phone = phone,
                content = content
            )
            contact.save()
            messages.success(request, "Your message has been send")

    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains = query)
        allPostsContent = Post.objects.filter(content__icontains = query)
        allPostsAuthor = Post.objects.filter(author__icontains = query)
        allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)

    if allPosts.count() == 0:
        messages.warning(request, "No Serch result found")
    params = {'allPosts':allPosts, 'query': query}
    return render(request, 'home/search.html', params)

def handleSignup(request):
    if request.method == 'POST':
        # Gets Post Parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for error inputs

        # Username should be under 10 char
        if len(username) > 10:
            messages.error(request, "Your Username must be under 10 character")
            return redirect('/')

        # Username should only contain letters & numbers
        if not username.isalnum():
            messages.error(request, "Your Username should contain letters & numbers")
            return redirect('/')

        # Pass1 and Pass2 should match
        if pass1 != pass2:
            messages.error(request, "Your Password do not match")
            return redirect('/')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('/')

    else:
        return render(request, '404.html')

def handleLogin(request):
    if request.method == 'POST':
        # Gets Post Parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('/')

    return render(request, '404.html')

def handleLogout(request):
    logout(request)
    messages.success(request, "You have been Successfully Logged out")
    return redirect('/')