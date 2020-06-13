from rest_framework import serializers
from article.models import ArticlePost,Category
from django.contrib.auth.models import User
import redis
from django_redis import get_redis_connection




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')


class ArticlePostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = ArticlePost
        fields = ['id','title','excerpt','category','created','author',]

class ArticleRetrieveSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()
    toc = serializers.CharField()
    body_html = serializers.CharField()

    class Meta:
        model = ArticlePost
        fields = [
            'id','title','toc','body_html','body','created','updated','category','author',
        ]

#
# class AddHistorySerializer(serializers.Serializer):
#     his_id = serializers.IntegerField(label='文章id',min_value=1)
#
#     def validate_article_id(self, value):
#         try:
#             ArticlePost.objects.get(id=value)
#         except ArticlePost.DoesNotExist:
#             raise serializers.ValidationError("文章不存在")
#         return value
#
#     def create(self,validated_data):
#         user_id = self.context['request'].user.id
#         article_id = validated_data['his_id']
#         conn = get_redis_connection('default')
#         pl = conn.pipeline()
#         conn.lrem("default_%s"% user_id,0,validated_data['his_id'])
#         conn.lpush("default_%s"% user_id,validated_data['his_id'])
#         conn.ltrim('default_%s'% user_id,0,6)
#
#         pl.execute()
#
#         return validated_data
#
