from rest_framework import serializers
from .models import Book


# モデルのようにクラスを作成していく
class BookSerializer(serializers.ModelSerializer):
    class Meta:  # このクラスからオブジェクトを作るとJSONなどに変換しやすいという理解で。
        model = Book
        fields = ['title', 'author']
