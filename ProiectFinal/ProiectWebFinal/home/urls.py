from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.CreateHomeView.as_view(), name='home'),
    path('about', views.CreateAboutView.as_view(), name='about'),
]