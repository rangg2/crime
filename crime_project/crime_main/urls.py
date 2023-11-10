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
    path('search_jong/', views.search_jong, name='search_jong'),
    path('search_bio/', views.search_bio, name='search_bio'),
    path('search_group/', views.search_group, name='search_group'),
    path('search/23114002/', views.search_report1, name='search_report1'),
    path('search/24105397/', views.search_report2, name='search_report2'),
    path('search/24105714/', views.search_report3, name='search_report3'),
    path('search/24105822/', views.search_report4, name='search_report4'),
    path('search/24115233/', views.search_report5, name='search_report5'),
    path('search/2485591/', views.search_report6, name='search_report6'),
    path('search_newsone/', views.search_news, name='news'),
    path('search_newstwo/', views.search_news2, name='news2'),
    path('search_newsthree/', views.search_news3, name='news3'),
    path('search_kang/', views.search_kang, name='search_kang'),
    path('search_kim/', views.search_kim, name='search_kim'),
    path('search_jung/', views.search_jung, name='search_jung'),
    path('search_ahn/', views.search_ahn, name='search_ahn'),
    path('search_kwang/', views.search_kwang, name='search_kwang'),
    path('search_yu/', views.search_yu, name='search_yu'),
]