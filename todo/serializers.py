from rest_framework import serializers
from .models import Todo

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class TareaIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']

class TareaTituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title']

class TareaUserIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user_id']
