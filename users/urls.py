from django.conf.urls import url
from django.urls import path, include
from . import views
from .api_views  import RegisterApiView, LoginApiView



app_name = 'users'


api_urls = [
    url(r'register/$', RegisterApiView.as_view()),
    url(r'login/$', LoginApiView.as_view())
]







urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
     path('api/', include(api_urls)),
    
    
]
