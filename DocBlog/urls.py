"""DocBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from appli1.views import login_user, logout_user, signup

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('appli1/', include("appli1.urls")),
    path('admin/', admin.site.urls),
    # path('fonction1', views.fonction1),
    path('fonction2', views.fonction2, name="script"),
    # path('fonction3', views.fonction3, name="script2"),
    # path('page_france/', views.page_france, name="france"),
    # path('page_usa/', views.page_usa, name="usa"),
    path('finish/', views.finish, name="finish"),
    path('signup/', signup, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('login/', login_user, name="login"),

    

]

