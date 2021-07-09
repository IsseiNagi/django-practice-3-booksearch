from django.urls import path
from .views import BookList, BookDetailView

urlpatterns = [
    path('list/', BookList.as_view(), name='list'),
    path('detail/<int:pk>/', BookDetailView.as_view()),
]
