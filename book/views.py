from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from .models import Book, Weather
from .serializers import BookSerializer, BookQuerySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class BookList(ListView):
    template_name = 'list.html'
    model = Book #どのデータベースを使用していくかの指定

class Topview(ListView):
    template_name = 'list.html'
    model = Book #どのデータベースを使用していくかの指定

class WeatherDetailView(DetailView):
    model = Weather
    template_name = 'detail.html'

class BookListAPI(ListCreateAPIView):
    queryset = Book.objects.all() #Bookクラスの中のデータをすべて持ってくる。これだけだとうまくＪＳＯＮとかに変換できないのでserializerをしようする
    serializer_class = BookSerializer #serializerを使わないとうまく変換できないので定義
    permission_classes = [IsAuthenticated] #認証機能


class SampleAPI(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookQuerySerializer #

    def create(self, request, *args, **kwargs):
        #受け取ったデータをシリアライザーに渡し、バリデーションを行います。
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        #バリデーションが通ったデータから,検索に必要なパラメータを取得します。
        title = serializer.validated_data['title'] #titleはAPIのボディにあるフィールドを指す

        #取得したパラメータをもとにデータベースをクエリして、該当する本のリストを取得
        books = Book.objects.filter(title__icontains=title)

        #取得した本のリストをシリアライズ
        book_serializer = BookSerializer(books, many=True)
        return Response(book_serializer.data, status=status.HTTP_200_OK)


