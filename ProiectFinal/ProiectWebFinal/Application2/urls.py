from django.urls import path

from Application2 import views

app_name = 'finance'

urlpatterns = [
    path('', views.ForwardRevenuesView.as_view(), name='revenues_list'),
    path('<int:pk>/reassign_engineer/', views.ReassignEngineerView.as_view(), name='reassign_engineer'),
    path('<int:pk>/generate_invoice/', views.generate_invoice, name='generate_invoice'),
    path('<int:pk>/download_invoice/', views.download_invoice, name='download_invoice'),
    # path('add/', views.CreateProjectsView.as_view(), name='add_project'),
    # path('<int:pk>/update/', views.UpdateProjectsView.as_view(), name='modify_project'),
    # path('<int:pk>/delete/', views.delete_project, name='delete_project'),
    # path('<int:pk>/activate/', views.activate_project, name='activate_project'),
    # path('<int:pk>/run_quote/', views.run_quote, name='generate_quote'),
    # path('<int:pk>/dl_and_refresh/', views.dl_and_refresh, name='dl_and_refresh'),
    # path('<int:pk>/quote_accepted/', views.quote_accepted, name='quote_accepted'),
    # path('<int:pk>/generate_report/', views.generate_report, name='generate_report'),
    path('revenues', views.DoneRevenuesView.as_view(), name='completed_work')
    # path('rundocx/', name='generate_doc_report'),
]