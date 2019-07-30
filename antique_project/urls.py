"""antique_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from antique_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('add/', views.add , name='add'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('category/', views.category, name='category'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('detail/<int:pk>', views.detail , name='detail'),
    path('catdetail/<int:pk>', views.catdetail , name='catdetail'),
    path('delete_item/<int:pk>', views.delete_item , name='delete_item'),
    path('item/<int:pk>/update', views.ItemUpdate.as_view() , name='updateitem'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
