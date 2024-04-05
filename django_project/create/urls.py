from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
    path("", views.create, name="create-home"),
    path("creat/", views.creat, name="create-creat"),
    path("login/", views.loginPage, name="create-login"),
    path("feed/", PostListView.as_view(), name="create-feed"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="create-post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="create-post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="create-post-delete"),
    path("post/new/", PostCreateView.as_view(), name="create-post"),
    path("profile/", views.profile, name="create-profile"),
    path("logout/", views.LogoutPage, name="create-logout"),
    path("helpline/", views.helpline, name="create-helpline"),
    
]

