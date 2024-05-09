from django.urls import path 

from user_data import views


urlpatterns=[
    path('login/',views.handlelogin,name="login"),
    path('signup/',views.signup,name="signup"),

]
