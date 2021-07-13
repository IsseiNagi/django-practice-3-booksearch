from django.shortcuts import render
from django.views.generic import ListView, DetailView
# from rest_framework.views import APIView  # APIを確認するため
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Create your views here.


class BookList(ListView):
    template_name = 'list.html'
    model = Book


class BookDetailView(DetailView):
    template_name = 'detail.html'
    model = Book


# APIを確認するため
# class BookListAPI(APIView):
    # permission_classes = []  # htmlを指定しなくても動くことを確認するために記載。


class BookListAPI(ListCreateAPIView):
    queryset = Book.objects.all()  # Bookモデルの中の全てのオブジェクトを取得する（モデルデータがないとエラーが出る）
    serializer_class = BookSerializer  # 取得したオブジェクトをJSONなどに変換するserializerを指定する。
    permission_classes = [IsAuthenticated]  # 認証指定。IsAuthenticatedはログイン済かどうか。
