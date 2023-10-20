from django.urls import path

from book.views import BookApiView

urlpatterns = [
    path('list/', BookApiView.as_view())
]