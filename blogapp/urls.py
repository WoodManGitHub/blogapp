from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.index, name='index'),
	path('post/<int:pk>/', views.detail, name='detail'),
	re_path('archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', views.archives, name='archives'),
	path('category/<int:pk>/', views.category, name='category')
]
