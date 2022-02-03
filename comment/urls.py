from django.urls import path
from .import views


app_name = 'comment'


urlpatterns = [
    path('get_all/', views.CommentListView.as_view()),
    path('comment/create/', views.CommentCreateView.as_view()),
    path('comment/update/<int:pk>/', views.CommentUpdateView.as_view()),
    path('comment/delete/<int:pk>/', views.CommentDeleteView.as_view()),

]