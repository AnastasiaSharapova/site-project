from django.urls import path
from . import views


urlpatterns = [
   path('', views.index,name='home'),
   path('about',views.about,name='about'),
   path('contact',views.contact,name='contact'),
   path('register',views.register_request,name='register'),
   path('account',views.login_request,name='account'),
   path('logout',views.logout_request,name='logout')

]