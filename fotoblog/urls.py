"""
URL configuration for fotoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True),
        name='login'),  #display de the login form and handle the login action
    path('logout/', LogoutView.as_view(), name='logout'), #logout the user, the logout button has to be a form using the post request
    path('home/', blog.views.home, name='home'),
    path('change_password/', PasswordChangeView.as_view(template_name='authentication/change_password.html'), name='change_password'),
    path('change_password_done/', PasswordChangeDoneView.as_view(template_name='authentication/password_change_done.html'), name='change_password_done'),
]
