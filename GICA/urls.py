"""GondarInternational_CharityAssociation URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("", views.index, name="home"),
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
    path('project/', views.project, name='project'),
    path('project1/', views.allproject.as_view(), name='project1'),
    path('allpayment/', views.payment_list.as_view(), name='allpayment'),
    path('news/', views.news_list.as_view(), name='news'),
    path('memberslist/', views.members_list.as_view(), name='memberslist'),
    path('islamicevents/', views.events_list.as_view(), name='islamicevents'),
    path('project2/', views.project2, name='project2'),
    path('project3/', views.project3, name='project3'),
    path('project4/', views.project4, name='project4'),
    path('news/', views.news, name='newsfeed'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
    path('donateniya/', views.donateniya, name='donateniya'),
    #path('pay/', views.pay, name='pay'),
    path('register/', views.register, name='register'),
    path("register_new", views.register_request, name="register_new"),
    path("login", views.login_request, name="login"),
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
