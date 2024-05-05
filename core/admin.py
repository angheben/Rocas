from django.contrib import admin
from .models import UserProfile, Post, Comment, Draft


# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile', 'created_on')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content', 'image', 'created_on')


@admin.register(Draft)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'image', 'content', 'created_on')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'body', 'date_added')
