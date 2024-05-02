from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField


class UserProfile(models.Model):
    user = models.CharField(User, max_length=30)
    profile = StdImageField(verbose_name='Image', upload_to='media', variations={
                            "thumb": {"width": 100, 'height': 100, 'crop': False}})
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="posts")
    image = StdImageField(verbose_name='Image', upload_to='media', variations={
                            "thumb": {"width": 225, 'height': 225, 'crop': False}})
    title = models.CharField(name="title", max_length=100)
    content = models.TextField(name="content", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Draft(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='draft_images')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
