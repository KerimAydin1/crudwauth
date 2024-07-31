# blog/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BlogPostListCreateView, BlogPostDetailView, RegisterUserView

urlpatterns = [
    path('blogs/', BlogPostListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogPostDetailView.as_view(), name='blog-detail'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
