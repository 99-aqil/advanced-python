from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.BlogPostListView.as_view(), name='post-list'),
    path('posts/create/', views.BlogPostCreateView.as_view(), name='post-create'),
    path('posts/<int:post_id>/comment/', views.CommentCreateView.as_view(), name='comment-create'),
    path('registration/', views.UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', views.UserLoginAPIView.as_view(), name='user-login'),
]
