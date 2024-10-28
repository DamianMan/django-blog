from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(), name='home'),
    path('login',views.LoginView.as_view(), name='login'),
    path('sign-up',views.SignUpView.as_view(), name='sign-up'),
    path('logout',views.LogoutView.as_view(), name='logout'),
    path('add-read-later', views.AddRemoveReadLaterView.as_view(), name='read_later'),
    path('read-later-posts', views.ReadLaterView.as_view(), name='read_later_posts'),
    path('posts', views.PostsView.as_view(), name='blog_posts'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='single_post'),
    path('post-comment/<int:id>', views.PostCommentView.as_view(), name='post_comment'),

]
