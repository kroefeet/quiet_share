from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<username>/', views.user_page, name='dashboard'),
    path('delete-profile/<username>', views.delete_profile),
]
