# Generated by Django 3.0.7 on 2020-06-08 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20200608_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='top',
            field=models.BooleanField(default=False, verbose_name='置顶'),
        ),
    ]
