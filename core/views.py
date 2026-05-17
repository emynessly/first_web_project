from django.shortcuts import render
from .models import Book

def top(request):
    top = [
            {"title": "1984", "author": "Джордж Оруэлл"},
            {"title": "Мы", "author": "Евгений Замятин"},
            {"title": "451 градус по Фаренгейту", "author": "Рэй Брэдбери"},
        ]
    context = {
        'top': top,
    }
    return render(request, 'core/top.html', context)

def index(request):
    context = {
        'title': 'Добро пожаловать в Мир книг!',
        'welcome_text': '<i>«Мир книг»</i> — каталог книг для читателей всех возрастов. '
            'Здесь собраны произведения разных жанров: от классики до современной прозы. '
            'Добавляйте книги в избранное, оставляйте отзывы и находите новые истории для души.'
    }
    return render(request, 'core/index.html', context)

def catalog(request):
    books = Book.objects.all()
    
    context = {
        'title': 'Каталог Книг',
        'books': books,
    }
    return render(request, 'core/catalog.html', context)