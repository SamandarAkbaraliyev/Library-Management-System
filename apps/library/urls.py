from django.urls import path
from apps.library import api_endpoints

urlpatterns = [
    path("books/", api_endpoints.BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", api_endpoints.BookRetrieveUpdateDestroyView.as_view(), name="book-crud"),
    path("books/<int:pk>/rate/", api_endpoints.RateBookView.as_view(), name="book-rate"),

    path('genres/<int:pk>/', api_endpoints.GenreDeleteView.as_view(), name='genre-delete'),

    path("authors/", api_endpoints.AuthorListCreateView.as_view(), name="author-list-create"),
    path("authors/<int:pk>/", api_endpoints.AuthorCRUDView.as_view(), name="author-crud"),
]