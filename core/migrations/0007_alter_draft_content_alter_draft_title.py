# Generated by Django 5.0.4 on 2024-05-04 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_post_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='draft',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='title'),
        ),
    ]
