# Generated by Django 5.1.2 on 2024-10-22 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(to='blog.comment'),
        ),
    ]
