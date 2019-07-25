from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    path('file/', views.file, name='file'),
    path('user/<username>/', views.user_page, name='view_profile'),
    #path('login/', views.login, name='login'),
    # path('signup/', views.signup, name='signup')
]
