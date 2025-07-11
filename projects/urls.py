from django.urls import path
from . import views

app_name = 'projects' # This is important for template tags

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
]