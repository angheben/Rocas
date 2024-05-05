from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = StdImageField(verbose_name='Image', upload_to='media', variations={
                            "thumb": {"width": 200, 'height': 200, 'crop': False}})
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    image = StdImageField(verbose_name='Image', upload_to='media', variations={
                            "thumb": {"width": 225, 'height': 225, 'crop': False}})
    title = models.CharField(name="title", max_length=100)
    content = models.TextField(name="content", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)


class Draft(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="drafts")
    title = models.CharField(max_length=100, name="title", verbose_name="title", blank=True)
    image = StdImageField(verbose_name='Image', upload_to='draft_images', variations={
        "thumb": {"width": 225, 'height': 225, 'crop': False}}, null=True, blank=True)
    content = models.TextField(name="content", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.post}'
