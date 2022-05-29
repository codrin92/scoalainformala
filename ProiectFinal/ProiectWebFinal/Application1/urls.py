from django.urls import path

from Application1 import views

app_name = 'reportwriter'

urlpatterns = [
    path('', views.ReportsView.as_view(), name='lista_rapoarte'),
    path('add/', views.CreateReportsView.as_view(), name='add_report'),
    path('<int:pk>/update/', views.UpdateReportsView.as_view(), name='modify_report'),
]