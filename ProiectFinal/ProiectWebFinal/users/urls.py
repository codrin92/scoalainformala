from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('new_account/', views.CreateNewAccount.as_view(), name='new_engineer'),
]