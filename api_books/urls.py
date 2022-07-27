from django.contrib import admin
from django.urls import path

from api_books.core.views import authors, books, book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authors', authors, name='authors'),
    path('api/books', book_list, name='book_list'),
    path('api/books/<int:id>', books, name='books')
]
