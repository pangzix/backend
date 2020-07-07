from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    name = models.CharField(max_length=50,verbose_name='分类')
    content = models.TextField(verbose_name='事件')
    color = models.CharField(max_length=200,verbose_name='颜色')
    start = models.DateTimeField(default='',verbose_name='开始时间')
    end = models.DateTimeField(default='',verbose_name='结束时间')
    add_time = models.DateField(auto_now_add=True,verbose_name='添加时间')
    flag = models.BooleanField(default=False,verbose_name='是否完成')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = '日程'
        verbose_name_plural = verbose_name

