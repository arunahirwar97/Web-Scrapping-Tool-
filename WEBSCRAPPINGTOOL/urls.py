"""AUTOCODEGENERATOR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from webscrapping_tool import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name="index"),
    path("all_a_url/",views.all_a_url , name="all_a_url"),    
    path("all_img_links/",views.all_img_links , name="all_img_links"),    
    path("get_table_data/",views.get_table_data , name="get_table_data"),    
    path("get_heading_data/",views.get_heading_data , name="get_heading_data"),    
    path("get_paragraph_data/",views.get_paragraph_data , name="get_paragraph_data"),    
    path("website_download/",views.website_download , name="website_download"), 
    path("get_list_data/",views.get_list_data , name="get_list_data"),    

]
