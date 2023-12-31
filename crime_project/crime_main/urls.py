from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('search/', views.search, name='search'),
    # path('search_jo/', views.search_jo, name='search_jo'),
    # path('search_pok/', views.search_pok, name='search_pok'),
    # path('search_est/', views.search_est, name='search_est'),
    # path('search_diff/', views.search_diff, name='search_diff'),
    # path('search_bang/', views.search_bang, name='search_bang'),
    # path('search_jong/', views.search_jong, name='search_jong'),
    # path('search_jang/', views.search_jang, name='search_jang'),
    # path('search_dead/', views.search_dead, name='search_dead'),
    # path('search_bio/', views.search_bio, name='search_bio'),
    # path('search_group/', views.search_group, name='search_group'),
    # path('search/23114002/', views.search_report1, name='search_report1'),
    # path('search/24105397/', views.search_report2, name='search_report2'),
    # path('search/24105714/', views.search_report3, name='search_report3'),
    # path('search/24105822/', views.search_report4, name='search_report4'),
    # path('search/24115233/', views.search_report5, name='search_report5'),
    # path('search/24119932/', views.search_report7, name='search_report7'),
    # path('search/2485591/', views.search_report6, name='search_report6'),
    # path('search_newsone/', views.search_news, name='news'),
    # path('search_newstwo/', views.search_news2, name='news2'),
    # path('search_newsthree/', views.search_news3, name='news3'),
    # path('search_kang/', views.search_kang, name='search_kang'),
    # path('search_kim/', views.search_kim, name='search_kim'),
    # path('search_jung/', views.search_jung, name='search_jung'),
    # path('search_ahn/', views.search_ahn, name='search_ahn'),
    # path('search_kwang/', views.search_kwang, name='search_kwang'),
    # path('search_yu/', views.search_yu, name='search_yu'),
    # path('search_jung_song/', views.search_jung_song, name='search_jung_song'),
    # path('search_ahn_so/', views.search_ahn_so, name='search_ahn_so'),
    # path('search_kim_lee/', views.search_kim_lee, name='search_kim_lee'),
    # path('search_kang_sung/', views.search_kang_sung, name='search_kang_sung'),
    path('list/', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path("", views.custom_login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.custom_logout, name="logout"),
    path('search2/', views.search_crime, name='search_crime'),
    path('search/', views.sbar, name='main'),
    path('crime/<int:crime_id>/', views.crime_image, name='crime_image'),
]