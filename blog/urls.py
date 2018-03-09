from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view(), name='details'),
]