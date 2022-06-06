from django.urls import path

from Application1 import views

app_name = 'reportwriter'

urlpatterns = [
    path('', views.ProjectsView.as_view(), name='project_list'),
    path('add/', views.CreateProjectsView.as_view(), name='add_project'),
    path('<int:pk>/update/', views.UpdateProjectsView.as_view(), name='modify_project'),
    path('<int:pk>/assign_engineer/', views.AssignEngineerView.as_view(), name='assign_engineer'),
    path('<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('<int:pk>/activate/', views.activate_project, name='activate_project'),
    path('<int:pk>/run_quote/', views.run_quote, name='generate_quote'),
    path('<int:pk>/download_quote/', views.download_quote, name='download_quote'),
    path('<int:pk>/quote_accepted/', views.quote_accepted, name='quote_accepted'),
    path('<int:pk>/generate_report/', views.generate_report, name='generate_report'),
    path('<int:pk>/download_report/', views.download_report, name='download_report'),
    path('closed_projects', views.ProjectsClosedView.as_view(), name='closed_projects'),
    # path('rundocx/', name='generate_doc_report'),
]