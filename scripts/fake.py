import os
import pathlib
import random
import sys
from datetime import timedelta

import django
import faker
from django.utils import timezone


back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","backend.settings")
    django.setup()

    from article.models import ArticlePost,Category
    from django.contrib.auth.models import User

    print('clean database')
    ArticlePost.objects.all().delete()
    Category.objects.all().delete()
    User.objects.all().delete()

    print('create a blog user')
    user = User.objects.create_superuser('admin','11@11.com','admin')

    tag_list = ['django','python','pipenv','docker','nginx','linux']
    category_list = ['python','note','tools','test']
    a_year_ago = timezone.now() -  timedelta(days=365)

    print('create categories and tags')
    for cate in category_list:
        Category.objects.create(name=cate)

    print('create a markdown sampe post')
    ArticlePost.objects.create(
        title = 'Markdown 代码高亮测试',
        body = pathlib.Path(BASE_DIR).joinpath('scripts','md.sample').read_text(encoding='utf-8'),
        category=Category.objects.create(name='Markdown测试'),
        author = user,
    )

    print('create some faked posts published within the past year')
    fake = faker.Faker()
    for _ in range(100):
        cate = Category.objects.order_by('?').first()
        created = fake.date_time_between(start_date='-1y',end_date='now',tzinfo=timezone.get_current_timezone())
        post = ArticlePost.objects.create(
            title=fake.sentence().rstrip('.'),
            body='\n\n'.join(fake.paragraphs(10)),
            created=created,
            category=cate,
            author=user,
        )
        post.save()

    fake = faker.Faker('zh_CN')
    for _ in range(100):  # Chinese
        cate = Category.objects.order_by('?').first()
        created_time = fake.date_time_between(start_date='-1y', end_date="now",
                                              tzinfo=timezone.get_current_timezone())
        post = ArticlePost.objects.create(
            title=fake.sentence().rstrip('.'),
            body='\n\n'.join(fake.paragraphs(10)),
            created=created,
            category=cate,
            author=user,
        )
        post.save()

    print('done!')
