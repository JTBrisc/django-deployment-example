"""learning_templates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# Importing views from our application ( i.e. 'basic_app' folder): we are 
# directly calling it from the function (*1*)
from basic_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # (*1*)one way to do this: when user comes to domain page at 127.0.0/8000 it 
    # will say: go to 'views' grab the 'index' and show it to this person on the 
    # 'home' page (i.e. index.html).
    path('',views.index, name='index'),
    
    # anything that starts with 'basic_app/': if someone goes to our Web page/basic_app 
    # and then the name of actual page or the view (ex: basic_app/relative, or basic_app/other 
    # or basic_app/etcetra...) then we tell it to go to the 'basic_app/urls.py' page 
    # for the subsequent views to show, or the subsequent mapping of the urls.    
    path('basic_app/', include('basic_app.urls'))
]
