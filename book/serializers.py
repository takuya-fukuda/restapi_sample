from rest_framework import serializers
from .models import Book

class BookQuerySerializer(serializers.Serializer):
    title = serializers.CharField(required=True) #titleのフィールドがシリアライザーに含まれているかをチェックする

class BookSerializer(serializers.ModelSerializer):
    class Meta: #Bookserializerがメタというクラスのインスタンスになる
        model = Book #どのテーブルをりようするか
        fields = ['title', 'author'] #どのデータfieldを使用するか