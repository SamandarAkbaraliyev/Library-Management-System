from django.urls import path
from apps.library import api_endpoints

urlpatterns = [
    path("books/", api_endpoints.BookListCreateView.as_view(), name="book-list-create"),
]