from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_logIn, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('addBlog/', views.add_blog, name='addBlog'),
    path('blog_detail/<int:id>', views.blog_detail, name='blogDetail'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('register/', views.user_register, name='register'),
]