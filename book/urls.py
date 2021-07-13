from django.urls import path
from .views import BookList, BookDetailView, BookListAPI

urlpatterns = [
    path('list/', BookList.as_view(), name='list'),
    path('detail/<int:pk>/', BookDetailView.as_view()),

    # apiviewだけ分けて記載するも良い。今回は比較のため、urls.pyに追記する。
    path('api/', BookListAPI.as_view()),
]
