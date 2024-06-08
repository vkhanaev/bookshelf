from django.contrib import admin
from django.urls import path

from books.views import show_books, show_book, show_books_json, show_book_json

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', show_books),
    path('books/<int:book_id>/', show_book),
    path('api/books/', show_books_json),
    path('api/books/<int:book_id>/', show_book_json),
]
