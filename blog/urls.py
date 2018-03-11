from django.urls import path
from django.views.decorators.http import require_POST

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog_index'),
    path('<int:pk>/', views.PostDetail.as_view(), name='blog_details'),
    path('archive/<int:month>/<int:year>/', views.ArchiveList.as_view(), name='archive_list'),
]