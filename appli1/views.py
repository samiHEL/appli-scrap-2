from imaplib import _Authenticator
from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login, logout, authenticate

User = get_user_model()

def index(request):
    return render(request, "appli1/index.html")
def article(request, numero_article):
    if numero_article in [1, 2, 3]:

    #Utilisation des fstring pour pouvoir inserer chaine de caractere
        return render(request, f"appli1/article_{numero_article}.html")
    return render(request, "appli1/article_not_found.html")
def signup(request):

    if request.method == "POST":
        username =request.POST.get("username")
        password =request.POST.get("password")
        user= User.objects.create_user(username=username,password=password)

        login(request, user)
        return redirect('index')
    return render(request, 'appli1/signup.html')

def logout_user(request):
   logout(request)
   return redirect('index') 
def login_user(request):
    if request.method == "POST":
        #Connecter l'user
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'appli1/login.html')