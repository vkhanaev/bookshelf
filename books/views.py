import json

from django.core import serializers
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, get_object_or_404

from books.models import Book


def show_books(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "books/books.html", context=context)


def show_book(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    context = {"book": book}
    return render(request, "books/book-description.html", context=context)


def convert_book_to_json(book: Book) -> json:
    return {
            "title": book.title,
            "author_full_name": book.author_full_name,
            "year_of_publishing": book.year_of_publishing,
            "copies_printed": book.copies_printed,
            "short_description": book.short_description,
    }


def show_books_json(request: HttpRequest) -> JsonResponse:
    books = Book.objects.all()
    books = [
        convert_book_to_json(book)
        for book in books
    ]
    return JsonResponse({"books": books},  json_dumps_params={'ensure_ascii': False})


def show_book_json(request: HttpRequest, book_id: int) -> JsonResponse:
    book = Book.objects.get(pk=book_id)
    book = convert_book_to_json(book)
    return JsonResponse(book, json_dumps_params={'ensure_ascii': False})
