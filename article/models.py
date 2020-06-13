from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
import markdown
from django.utils.html import strip_tags
from markdown.extensions.toc import TocExtension
import re
from django.utils.functional import cached_property
from django.utils.text import slugify



class Category(models.Model):
    name = models.CharField('分类',max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


def generate_rich_content(value):
    # https: // www.zmrenwu.com /
    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            TocExtension(slugify=slugify),
        ]
    )
    content = md.convert(value)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s</div>',md.toc,re.S)
    toc = m.group(1) if m is not None else ""
    return {"content":content,"toc":toc}

class ArticlePost(models.Model):

    author = models.ForeignKey( User,on_delete=models.CASCADE,verbose_name='作者')
    title = models.CharField('标题',max_length=100)
    excerpt = models.CharField('摘要',max_length=200,blank=True)
    tags = TaggableManager(verbose_name='标签',blank=True)
    category =models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类')
    body = models.TextField('正文')
    created = models.DateTimeField('创建日期',default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    top = models.BooleanField('置顶',default=False)




    def save(self,*args,**kwargs):
        self.modified_time = timezone.now()

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',

        ])

        self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args,**kwargs)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.title

    # https: // www.zmrenwu.com /
    @property
    def toc(self):
        return self.rich_content.get("toc","")

    @property
    def body_html(self):
        return self.rich_content.get("content","")

    @cached_property
    def rich_content(self):
        return generate_rich_content(self.body)
