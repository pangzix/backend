# Generated by Django 3.0.7 on 2020-06-11 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_articlepost_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='avatar',
            field=models.CharField(max_length=500, verbose_name='文章标题图'),
        ),
    ]
