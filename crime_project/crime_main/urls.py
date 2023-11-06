from django.contrib import admin
from django.urls import path, include
from . import views

# handler404 = 'crime_main.views.custom_404'

urlpatterns = [
    path('', views.main, name='main'),
    path('search/', views.search, name='search'),
    path('search_results/', views.search_results, name='search_results'),
    path('search_results2/', views.search_results2, name='search_results2'),
]