# Generated by Django 2.1.2 on 2018-11-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blog_like_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=255, verbose_name='内容'),
        ),
    ]
