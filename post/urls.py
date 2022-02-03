from django.urls import path, include
from . import views 
from .import api_views


app_name = 'post'



api_urls = [
    path('posts/', api_views.PostListView.as_view()),
    path('posts/create/', api_views.PostCreateView.as_view()),
    path('posts/update/int:pk>/', api_views.PostUpdateView.as_view()),
    path('posts/delete/<int:pk>/', api_views.PostDeleteView.as_view()),
]





urlpatterns = [
    path('index/', views.PostList.as_view(), name='index'),
    path('post_delete/<int:p_id>/', views.PostDelete.as_view(), name='post_delete'),
    path('post_download/<str:key>/', views.PostDownload.as_view(), name='post_download'),
    path('api/', include(api_urls)),
]

