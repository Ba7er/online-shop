"""walladver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from registration_app import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
#from django.contrib.auth import logout

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('cat_prod/',include('prod_cat_app.urls')),
    path('cart/',include('cart.urls')),
    path('admin/', admin.site.urls),
    path('',views.home_view, name='home_view'),
    path('loginpage/',views.login_view,name='loginview'),
    path('register/',views.signup_view,name='registerview'),
    path('home/',views.home_page,name='home_page'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('changepwd/',views.change_pwd,name='changepassword'),
    url(r'^password_reset/$',
        PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
        name='password_reset'),
    url(r'^password_reset/done/$',
        PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/done/$',
        PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
