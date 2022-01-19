from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    #link to database
    features = Feature.objects.all()
    return render(request, 'index.html', {'features' : features})

    """Simple models
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is very quick'
    feature1.isTrue = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'Our service is very reliable'
    feature2.isTrue = True

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy'
    feature3.details = 'Our service is very easy'
    feature3.isTrue = False

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.details = 'Our service is very affordable'
    feature4.isTrue = True

    features = [feature1, feature2, feature3, feature4]
    return render(request, 'index.html', {'features' : features})
    """

    """1.Simply test HttpResponse
    return HttpResponse("<h1>Hey, Welcome</h1>")
    """

    """2.Sending Data To Template File
    context = {
        'name' :'Spyder',
        'age' : 40,
        'country' : 'Taiwan',
    }
    #render a django template
    return render(request, 'index.html', context)
    """

    """3.Building A Word Counter In Django
    return render(request, 'index.html')
    """

#3.Building A Word Counter In Django
def counter(request):
    #GET method
    #text = request.GET["text"]
    #POST method
    text = request.POST["text"]
    amountOfWords = len(text.split())
    return render(request, 'counter.html', context={'amount' : amountOfWords})

#User Registration
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "User Already Used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password not the Same")
            return redirect('register')
    else:
        return render(request, 'register.html')

#User Login and Logout
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/') #To home page
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk' : pk})

def counter(request):
    posts = [1,2,3,4,5,'tim','tom','john']
    return render(request, 'counter.html', {'posts' : posts})
