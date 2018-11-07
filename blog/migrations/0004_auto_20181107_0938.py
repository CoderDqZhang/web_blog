# Generated by Django 2.1.2 on 2018-11-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181015_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='read_number',
            field=models.PositiveIntegerField(default=0, verbose_name='阅读人数'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=266, verbose_name='标题'),
        ),
    ]
