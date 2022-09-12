from datetime import datetime
from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
import requests
from random import randint
import requests
from bs4 import BeautifulSoup
import time
import undetected_chromedriver.v2 as uc
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

User = get_user_model()


def index(request):
    date = datetime.today()
    # return HttpResponse("<h1>Test11</h1>")
    return render(request, "DocBlog/index.html", context={"date":date})
def finish(request):
    return render(request, "DocBlog/finish.html")

# def fonction1(request):
#     return render(request,'DocBlog/scrapp.html') 

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        user = User.objects.create_user(username=username,firstname=firstname,lastname=lastname,email=email,password=password,password1=password1)
        login(request, user) 
        # mon_utilisateur = User.objects.create(username, email, password)
        # mon_utilisateur.first_name=firstname
        # mon_utilisateur.last_name = lastname
        # mon_utilisateur.save()
        # messages.success(request, 'Votre compte a été crée avec success ')
        # return redirect('DocBlog/scrapp.html')
        return redirect('DocBlog/index')
    return render(request, 'DocBlog/register.html')

def login(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(username=username)
    return render(request, 'DocBlog/login.html')

def logout(request):
    pass


def fonction2(request):
    if request.method == 'POST':
        # créez une instance de formulaire + remplir avec les données de la requête :
        form = NameForm(request.POST)
        # Check si form est valid
        if form.is_valid():
            #recup donées
            pays=form.cleaned_data['pays']
            enseigne = form.cleaned_data['enseigne']
            scrap_choices=form.cleaned_data['scrap_choices']
            ville = form.cleaned_data['ville']
            departement = form.cleaned_data['departement']
            france=["france","France","fr","FR"]
            espagne=["espagne","Espagne","esp","Esp"]
            usa=["usa","etats-unis","Etats Unis"]
            pharma=["pharma","Pharma", "Pharmacie", "pharmacie"]

            if pays =="France" and enseigne not in pharma:
                
                driver = uc.Chrome()
                url = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui="+enseigne+"&ou="+departement+"&proximite=0&quoiQuiInterprete="+enseigne+"&contexte=X%2BOmMTxNwxNIRj1qIbnaueFojzuWysbjEy3zaBN/m%2Bg%3D&idOu=L09402800&page={page}"
                
                if scrap_choices=='20': pages = range(1, 2)
                elif scrap_choices=='100': pages = range(1, 6)
                elif scrap_choices=='500': pages = range(1, 26)
                else : pages = range(1, 53)
                with open('/home/veesion/Bureau/'+enseigne+'.csv', "w+") as f:
                    for page in pages:
                        driver.get(url.format(page=page))
                        time.sleep(3)    
                        phone_elements = driver.find_elements_by_css_selector("span[class='icon icon-phone']")
                        for phone_element in phone_elements:
                            phone_element.click()
                            time.sleep(1) 
                        soup = BeautifulSoup(driver.page_source, 'html.parser')
                        stores = soup.find_all("li", class_="bi bi-generic") 
                        for store in stores: 
                            try:
                                nom = store.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
                            except:
                                nom=""
                            try:    
                                adr= store.find("div", class_="bi-address small").text.replace("\n", "").strip()
                            except:
                                adr=""
                            try:
                                tel=store.find("div", class_="number-contact txt_sm").find("span").text.replace("\n", "").strip()
                            except:
                                tel = ""
                            print(f"{nom}; {adr}; {tel}", file=f)
                            print(f"{nom}; {adr};{tel}")
                            #fermer la page chrome
                        driver.close()
                        return render(request, "DocBlog/finish.html")
                            #return HttpResponse("<h1>Page scrappée Félicitation !!</h1>")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
                
                
                
        
            if pays=="Espagne":
                driver = uc.Chrome()
                url = "https://www.paginasamarillas.es/search/all-ac/all-ma/all-pr/all-is/all-ci/all-ba/all-pu/all-nc/{page}?what="+enseigne+"&aprob=0.0&nprob=1.0"
                if scrap_choices=='20': pages = range(1, 2)
                elif scrap_choices=='100': pages = range(1, 6)
                elif scrap_choices=='500': pages = range(1, 26)
                else : pages = range(1, 53)
                
                with open("/home/veesion/Bureau/"+enseigne+".csv", "w+") as f:
                    for page in pages:
                        driver.get(url.format(page=page))
                        time.sleep(2)
                        phone_elements = driver.find_elements_by_css_selector("div[class='llama-desplegable btn btn-amarillo btn-block showPhone']")
                        for phone_element in phone_elements:
                            phone_element.click()
                            time.sleep(1)
                        soup = BeautifulSoup(driver.page_source, 'html.parser')
                        stores = soup.find_all("div", class_="listado-item item-ig")
                        print(stores)
                        for store in stores:
                            nom="SUPERMERCADO BM URBAN".replace("\n", ";").strip()
                            try:
                                adr=store.find("div", class_="cuerpo-2").find("span", class_="location").text.replace("\n", ";").strip()
                            except:
                                adr = ""
                            try:
                                contact =store.find("a", class_="llama-desplegable btn btn-amarillo btn-block phone d-none").find("span").text.replace("\n", ";").strip()
                            except:
                                contact = ""
                            try:
                                adr2 =store.find("div", class_="cuerpo-2").find("p", class_="location").text.replace("\n", ";").strip()
                            except:
                                adr2 = ""
                            print(f"{nom}; {adr}; {adr2}; {contact}", file=f)
                            print(f"{nom}; {adr}; {adr2}, {contact}")
                        driver.close()
                        return render(request, "DocBlog/finish.html")


            if pays=="Etats-Unis":
                driver = uc.Chrome()
                url = "https://www.whitepages.com/business/NY/"+enseigne+"?page={page}"
                pages = range(1, 3)
                for page in pages:
                    driver.get(url.format(page=page))
                    time.sleep(3)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    stores = soup.find_all("a", class_="btn btn--large btn--outlined primary--text")
                    for store in stores:
                        url2="https://www.whitepages.com"+store["href"]
                        driver.get(url2)
                        soup = BeautifulSoup(driver.page_source, 'html.parser')
                        try:
                            tel = store.find("div", class_="d-flex flex-grow-1 justify-space-between").find("div").text.replace("\n", "").strip()
                        except:
                            tel=""
                        # try:
                        #     tel=store.find("div", class_="number-contact txt_sm").find("span").text.replace("\n", "").strip()
                        # except:
                        #     tel = ""
                        print(f"{tel}", file=f)
                        print(f"{tel}")
                        
                            # for store in stores: 
                            #     try:
                            #         nom = store.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
                            #     except:
                            #         nom=""
                            #     try:    
                            #         adr= store.find("div", class_="bi-address small").text.replace("\n", "").strip()
                            #     except:
                            #         adr=""
                            #     try:
                            #         tel=store.find("div", class_="number-contact txt_sm").find("span").text.replace("\n", "").strip()
                            #     except:
                            #         tel = ""
                                # print(f"{nom}; {adr}; {tel}", file=f)
                                # print(f"{nom}; {adr};{tel}")
                        return render(request, "DocBlog/finish.html")
            if enseigne in pharma:
                driver = uc.Chrome()
                url = "https://www.pharmarket.com/annuaire-pharmacies/ville/"+ville+"-"+departement
                with open("/home/veesion/Bureau/Pharma.csv", "w") as f:
                    driver.get(url)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    stores = soup.find_all("a", class_="newBtn accept")   
                    for store in stores: 
                        url1 = store["href"]
                        driver.get(url1)
                        sous = BeautifulSoup(driver.page_source, 'html.parser')
                        try:
                            adr=sous.find("span", class_="main").text.replace("\n", "").strip()
                        except:
                            adr=""
                        try:
                            tel=sous.find("div", class_="tel").text.replace("\n", "").strip()
                        except:
                            tel=""
                        name=sous.find("h1", class_="mainTitle title shopTitle").find("span").text.replace("\n", "").strip()
                        print(f"{name}; {adr}; {tel}", file=f)
                        print(f"{name}; {adr};{tel}")
                            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'DocBlog/scrapp.html', {'form': form})

def fonction3(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            enseigne = form.cleaned_data['enseigne']
            driver = uc.Chrome()
            url = "https://www.whitepages.com/business/NY/"+enseigne+"?page={page}"
            pages = range(1, 3)
            with open('/home/veesion/Téléchargements/scrappUSA.csv', "w+") as f:
                for page in pages:
                    driver.get(url.format(page=page))
                    time.sleep(3)    
                    phone_elements = driver.find_elements_by_css_selector("span[class='icon icon-phone']")
                    for phone_element in phone_elements:
                        phone_element.click()
                        time.sleep(1) 
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    stores = soup.find_all("li", class_="bi bi-generic") 
                    for store in stores: 
                        try:
                            nom = store.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
                        except:
                            nom=""
                        try:    
                            adr= store.find("div", class_="bi-address small").text.replace("\n", "").strip()
                        except:
                            adr=""
                        try:
                            tel=store.find("div", class_="number-contact txt_sm").find("span").text.replace("\n", "").strip()
                        except:
                            tel = ""
                        print(f"{nom}; {adr}; {tel}", file=f)
                        print(f"{nom}; {adr};{tel}")
            return HttpResponse("<h1>Page scrappée Félicitation !!</h1>")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'DocBlog/scrapp.html', {'form': form})
        # data=requests.get("https://reqres.in/api/users")
        # print(data.text)
        # data=data.text
        # return render(request,'DocBlog/index.html',{'data':data})
        



# def fonction2(request):
#     # data=requests.get("https://reqres.in/api/users")
#     # print(data.text)
#     # data=data.text
#     # return render(request,'DocBlog/index.html',{'data':data})
#     driver = uc.Chrome()
#     url = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=carrefour%20city&ou=Ile-de-France&idOu=R11&page=2&contexte=FArWdw1FM2Vg8/Rwqp%2BJRA%3D%3D&proximite=0&quoiQuiInterprete=carrefour%20city"
#     driver.get(url)
#     time.sleep(10) 
#     soup1 = BeautifulSoup(driver.page_source, 'html.parser')
#     stores1 = soup1.find("li", class_="bi bi-generic") 
#     noms = stores1.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
#     url1 = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui="+noms+"&ou=Ile-de-France&idOu=R11&page={page}&contexte=FArWdw1FM2Vg8/Rwqp%2BJRA%3D%3D&proximite=0&quoiQuiInterprete="+noms+""
#     pages = range(1, 26)
#     with open('C:/Users/samip/OneDrive/Documents/Scrapp/scrapp.csv', "w+") as f:
#         for page in pages:
#             driver.get(url1.format(page=page))
#             time.sleep(3)    
#             phone_elements = driver.find_elements_by_css_selector("span[class='icon icon-phone']")
#             for phone_element in phone_elements:
#                 phone_element.click()
#                 time.sleep(1) 
#             soup = BeautifulSoup(driver.page_source, 'html.parser')
#             stores = soup.find_all("li", class_="bi bi-generic") 
#             for store in stores: 
#                 try:
#                     nom = store.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
#                 except:
#                     nom=""
#                 try:    
#                     adr= store.find("div", class_="bi-address small").text.replace("\n", "").strip()
#                 except:
#                     adr=""
#                 try:
#                     tel=store.find("div", class_="number-contact txt_sm").find("span").text.replace("\n", "").strip()
#                 except:
#                     tel = ""
#                 print(f"{nom}; {adr}; {tel}", file=f)
#                 print(f"{nom}; {adr};{tel}")
# def fonction3(request):
#     # data=requests.get("https://reqres.in/api/users")
#     # print(data.text)
#     # data=data.text
#     # return render(request,'DocBlog/index.html',{'data':data})
#     driver = uc.Chrome()
#     url = "https://www.whitepages.com/business/NY/Nike"
#     driver.get(url)
#     time.sleep(10) 
#     soup1 = BeautifulSoup(driver.page_source, 'html.parser')
#     stores1 = soup1.find("li", class_="bi bi-generic") 
#     noms = stores1.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
#     url1 = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui="+noms+"&ou=Ile-de-France&idOu=R11&page={page}&contexte=FArWdw1FM2Vg8/Rwqp%2BJRA%3D%3D&proximite=0&quoiQuiInterprete="+noms+""
#     pages = range(1, 26)
#     with open('C:/Users/samip/OneDrive/Documents/Scrapp/scrapp.csv', "w+") as f:
#         for page in pages:
#             driver.get(url1.format(page=page))
#             time.sleep(3)    
#             phone_elements = driver.find_elements_by_css_selector("span[class='icon icon-phone']")
#             for phone_element in phone_elements:
#                 phone_element.click()
#                 time.sleep(1) 
#             soup = BeautifulSoup(driver.page_source, 'html.parser')
#             stores = soup.find_all("li", class_="bi bi-generic") 
#             for store in stores: 
#                 try:
#                     nom = store.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
#                 except:
#                     nom=""
#                 try:    
#                     adr= store.find("div", class_="bi-address small").text.replace("\n", "").strip()
#                 except:
#                     adr=""
#                 try:
#                     tel=store.find("div", class_="number-contact txt_sm").find("span").text.replace("\n", "").strip()
#                 except:
#                     tel = ""
#                 print(f"{nom}; {adr}; {tel}", file=f)
#                 print(f"{nom}; {adr};{tel}")
# def fonction4(request):
#     # data=requests.get("https://reqres.in/api/users")
#     # print(data.text)
#     # data=data.text
#     # return render(request,'DocBlog/index.html',{'data':data})
#     driver = uc.Chrome()
#     url = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=carrefour%20city&ou=Ile-de-France&idOu=R11&page=2&contexte=FArWdw1FM2Vg8/Rwqp%2BJRA%3D%3D&proximite=0&quoiQuiInterprete=carrefour%20city"
#     driver.get(url)
#     time.sleep(10) 
#     soup1 = BeautifulSoup(driver.page_source, 'html.parser')
#     stores1 = soup1.find("li", class_="bi bi-generic") 
#     noms = stores1.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
#     url1 = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui="+noms+"&ou=Ile-de-France&idOu=R11&page={page}&contexte=FArWdw1FM2Vg8/Rwqp%2BJRA%3D%3D&proximite=0&quoiQuiInterprete="+noms+""
#     pages = range(1, 26)
#     with open('C:/Users/samip/OneDrive/Documents/Scrapp/scrapp.csv', "w+") as f:
#         for page in pages:
#             driver.get(url1.format(page=page))
#             time.sleep(3)    
#             phone_elements = driver.find_elements_by_css_selector("span[class='icon icon-phone']")
#             for phone_element in phone_elements:
#                 phone_element.click()
#                 time.sleep(1) 
#             soup = BeautifulSoup(driver.page_source, 'html.parser')
#             stores = soup.find_all("li", class_="bi bi-generic") 
#             for store in stores: 
#                 try:
#                     nom = store.find("a", class_="bi-denomination pj-link").text.replace("\n", "").strip()
#                 except:
#                     nom=""
#                 try:    
#                     adr= store.find("div", class_="bi-address small").text.replace("\n", "").strip()
#                 except:
#                     adr=""
#                 try:
#                     tel=store.find("div", class_="number-contact txt_sm").find("span").text.replace("\n", "").strip()
#                 except:
#                     tel = ""
#                 print(f"{nom}; {adr}; {tel}", file=f)
#                 print(f"{nom}; {adr};{tel}")
  













#     driver = uc.Chrome()
#     url = "https://www.iga.com/find-a-store?page={page}"
#     pages = range(2, 5)
#     with open('C:/Users/samip/OneDrive/Documents/Scrapp/iga.csv', 'w+') as f:
#         for page in pages:
#             driver.get(url.format(page=page))
#             time.sleep(4)
#             soup = BeautifulSoup(driver.page_source,'html.parser')
#             stores = soup.find_all("div", class_="span8 store-location-details")
#             for store in stores:
#                 nom = store.find("h3").text.replace("\n", "").strip()
#                 # adresse = store.find("address", class_="store-address clearfix").text.replace("\n", "").strip()
#                 # try:
#                 #     tel=store.find("p", class_="store-phone-fax").find("a").text.replace("\n", "").strip()
#                 # except:
#                 #     tel = ""
#                 print(f"{nom}", file=f)
#                 print(f"{nom}")
#     return HttpResponse("<h1>Page scrappée Félicitation !!</h1>")
        
# #    




    # data=requests.get("https://www.google.com/")
    # print(data.text)
    # data=data.text
    # return render(request,'index.html',{'data':data})




   

            