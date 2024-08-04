from django.urls import path
from accounts.views import *
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    path('login/',login_view,name='login'),
    path('logout',logout_view,name='logout'),
    path('signup',signup_view,name='signup'),
    path("change-password/",auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('reset_password',resetpass,name='password_reset'),
    
]