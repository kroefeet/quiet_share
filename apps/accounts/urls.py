from django.urls import path

from apps.accounts import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.log_out, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('user/<username>/', views.view_profile, name='view_profile'),
]
