from django.urls import path

from book.views import BookListView, BookDeleteView, BookUpdateView, BookDetailView, BookCreateView

urlpatterns = [
    path('list/', BookListView.as_view()),
    path('list/<int:pk>/', BookDetailView.as_view()),
    path('update/<int:pk>/', BookUpdateView.as_view()),
    path('delete/<int:pk>/', BookDeleteView.as_view()),
    path('create/', BookCreateView.as_view()),
]