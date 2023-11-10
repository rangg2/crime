from django.contrib import admin
from django.urls import path, include
from . import views

# handler404 = 'crime_main.views.custom_404'

urlpatterns = [
    path('', views.main, name='main'),
    path('search/', views.search, name='search'),
    path('search_jo/', views.search_jo, name='search_jo'),
    path('search_pok/', views.search_pok, name='search_pok'),
    path('search_est/', views.search_est, name='search_est'),
    path('search_bang/', views.search_bang, name='search_bang'),
    path('search_newsone/', views.search_news, name='news'),
    path('search_newstwo/', views.search_news2, name='news2'),
    path('search_newsthree/', views.search_news3, name='news3'),
    # path('search_results2/', views.search_results2, name='search_results2'),
]