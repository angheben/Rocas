from django.urls import path
from .views import (MenuView, CreatePostView, DeletePostView, UpdatePostView, LogoutView, LoginView, SignUpView, ProfileView
                    , DraftsView, UpdateDraftView, DeleteDraftView, AddCommentView, CommentDeleteView, CommentUpdateView)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Menu Path
    path("", MenuView.as_view(template_name="menu.html"), name="menu"),

    # Create Post Path
    path("post", CreatePostView.as_view(template_name="post.html"), name="post"),

    # Paths for User actions
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("signup/", SignUpView.as_view(template_name="signup.html"), name="signup"),

    # Paths for Posts
    path("profile/", ProfileView.as_view(template_name="profile.html"), name="profile"),
    path("profile/post/<int:pk>", UpdatePostView.as_view(template_name="update_post.html"), name="update_post"),
    path("profile/post/delete/<int:pk>", DeletePostView.as_view(template_name="delete_post.html"), name="delete_post"),

    # Paths for Drafts
    path("drafts/", DraftsView.as_view(template_name="drafts.html"), name="drafts"),  # Add this line
    path("profile/drafts/update/<int:pk>", UpdateDraftView.as_view(template_name="update_draft.html"),
         name="update_draft"),
    path("profile/draft/delete/<int:pk>", DeleteDraftView.as_view(template_name="delete_draft.html"),
         name="delete_draft"),

    # Paths for comments
    path('add_comment/<int:post_id>/', AddCommentView.as_view(), name='add_comment'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
