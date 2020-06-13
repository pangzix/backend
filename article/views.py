from django.shortcuts import render
from django.http import HttpResponse
from article.models import ArticlePost,Category
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets,mixins,generics,permissions
from article.serializers import ArticlePostSerializer,UserSerializer,CategorySerializer,ArticleRetrieveSerializer
from .permissions import IsOwnerOrReadOnly
import django_filters



class ArticlesPagination(PageNumberPagination):
    page_size = 6 #默认每一页个数
    page_size_query_param = 'page_size'
    page_query_param = 'p' #参数?p=xx
    max_page_size = 50 #最大每页个数

# 筛选
class ArticleFilter(django_filters.rest_framework.FilterSet):
    category = django_filters.Filter(field_name="category__id")
    class Meta:
        model = ArticlePost
        fields = ['category',]


class TopArticlePostViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = ArticlePost.objects.filter(top=True)
    def get_serializer_class(self):
        if self.action == 'list':
            return ArticlePostSerializer
        elif self.action == 'retrieve':
            return ArticleRetrieveSerializer
        else:
            return super(ArticlePostViewSet,self).get_serializer_class()


class ArticlePostViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    # serializer_class = ArticlePostSerializer
    queryset = ArticlePost.objects.all().order_by('-created')
    pagination_class = ArticlesPagination
    filter_class = ArticleFilter
    def get_serializer_class(self):
        if self.action == 'list':
            return ArticlePostSerializer
        elif self.action =='retrieve':
            return ArticleRetrieveSerializer
        else:
            return super(ArticlePostViewSet, self).get_serializer_class()


# class UserHistoryViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
#     serializer_class = AddHistorySerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def post(self,request):
#         return self.create(request)
#
#     def get(self,request):
#         user_id = request.user.id
#         conn = get_redis_connection("default")
#         history = conn.lrange("default_%s" % user_id,0,6)
#         articles = []
#         for his_id in history:
#             article = ArticlePost.objects.get(id=his_id)
#             articles.append(article)
#
#         s = ArticlePostSerializer(articles,many=True)
#         return  HttpResponse(s.data)



