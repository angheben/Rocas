from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.CharField(User, max_length=30)
    profile = models.ImageField(name="profile", upload_to="profile_pictures") # I need to adjust the size of the image here
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="posts")
    image = models.ImageField(name="image", upload_to="post_pictures", null=True, blank=True)
    title = models.CharField(name="title", max_length=100)
    content = models.TextField(name="content", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
