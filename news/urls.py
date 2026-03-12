from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('category/<str:category>/', views.category_news, name='category_news'),
    path("search/", views.search_news, name="search_news"),
    path("latest-news/", views.latest_news),
]