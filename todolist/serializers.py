from rest_framework import serializers
from .models import TodoList

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = ('id','name','content','color','start','end','add_time','flag')
