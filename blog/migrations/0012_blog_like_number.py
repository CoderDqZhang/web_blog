# Generated by Django 2.1.2 on 2018-11-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20181108_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='like_number',
            field=models.PositiveIntegerField(default=0, verbose_name='喜欢人数'),
        ),
    ]