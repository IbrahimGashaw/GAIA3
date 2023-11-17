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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from GICA import views as users_view
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
admin.site.site_header = "GAIA Admin"
admin.site.site_title = "GAIA Admin Portal"
admin.site.index_title = "Welcome to GAIA Website"
urlpatterns = [
    path('', include('GICA.urls')),
    path("register_new", users_view.register_request, name="register_new"),
    path('register.html/', users_view.register, name='register'),
    path('project1/', users_view.allproject.as_view(), name='project1'),
    path('allpayment/', users_view.payment_list.as_view(), name='allpayment'),
    path('news/', users_view.news_list.as_view(), name='news'),
    path('memberslist/', users_view.members_list.as_view(), name='memberslist'),
    path('islamicevents/', users_view.events_list.as_view(), name='islamicevents'),
    path("login", users_view.login_request, name="login"),
    #path('pay.html/', user_views.pay, name='pay'),
    path('donate/', users_view.donate, name='donate'),
    path('donateniya/', users_view.donateniya, name='donateniya'),
    #path('member/', user_views.member, name='member'),
    path('login/', auth_views.LoginView.as_view(template_name='GICA/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='GICA/logout.html'), name='logout'),
   # path('<int:id>/', user_views.employee_form,name='employee_update'), # get and post req. for update operation
    #path('delete/<int:id>/',user_views.employee_delete,name='employee_delete'),
    path('list/',users_view.list,name='list'),# get req. to retrieve and display all records
    path("admin/", admin.site.urls),
    path("data-browser/", include("data_browser.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
