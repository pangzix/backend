# Generated by Django 2.2.13 on 2020-07-06 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=50, verbose_name='分类')),
                ('events', models.TextField(verbose_name='事件')),
                ('colors', models.CharField(max_length=200, verbose_name='颜色')),
                ('start_time', models.DateTimeField(default='', verbose_name='开始时间')),
                ('end_time', models.DateTimeField(default='', verbose_name='结束时间')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '日程',
                'verbose_name_plural': '日程',
            },
        ),
    ]