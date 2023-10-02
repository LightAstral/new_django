from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("blog/", views.index, name="main"),
    path("blog/post<int:id>", views.post, name="post"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("services", views.services, name="services"),
    path('blog/category/<str:name>', views.category, name='category'),
    path('blog/search/', views.search, name="search"),
    path('blog/create/', views.create, name="create"),
    path('blog/post<int:post_id>/add_comment', views.add_comment, name='add_comment'),
    path('blog/login', LoginView.as_view(), name='blog_login'),
    path('blog/logout', LogoutView.as_view(), name='blog_logout'),
    path('blog/user_profile/', views.user_profile, name='user_profile'),
    path('blog/edit_profile/', views.edit_profile, name='edit_profile'),
    path('blog/private_message/<str:username>/', views.private_message, name='private_message'),
]