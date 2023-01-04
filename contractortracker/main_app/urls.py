from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.client_index, name='index'),
    path('clients/new/', views.NewClient.as_view(), name='new_client'),
    path('clients/<int:client_id>/manage', views.manage_client, name='manage_client'),
    path('clients/<int:client_id>/manage/description/', views.add_task, name='add_task'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('accounts/signup/', views.SignUpForm.as_view(), name='signup'),

]