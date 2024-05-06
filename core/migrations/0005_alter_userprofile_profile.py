# Generated by Django 5.0.4 on 2024-05-04 19:31

import stdimage.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_post_id_alter_post_user_alter_userprofile_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='media', variations={'thumb': {'crop': False, 'height': 200, 'width': 200}}, verbose_name='Image'),
        ),
    ]