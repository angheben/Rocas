# Generated by Django 5.0.4 on 2024-05-02 17:32

import django.utils.timezone
import stdimage.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_content_alter_comment_user_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=stdimage.models.StdImageField(default=django.utils.timezone.now, force_min_size=False, upload_to='media', variations={'thumb': {'crop': False, 'height': 225, 'width': 225}}, verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='media', variations={'thumb': {'crop': False, 'height': 100, 'width': 100}}, verbose_name='Image'),
        ),
    ]
