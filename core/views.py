from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Book
from .forms import FeedbackForm, BookForm

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

def contact(request):    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            
            print("=" * 20)
            print("Новое сообщение:")
            print(f"Тема: {subject}")
            print(f"Email: {email}")
            print(f"Сообщение: {text}")
            print("=" * 20)
            return redirect('core:index')
    else:
        form = FeedbackForm()
    
    context = {
        'form': form,
        'title': 'Обратная связь'
    }
    return render(request, 'core/contact.html', context)

def catalog(request):
    books = Book.objects.all()
    
    context = {
        'title': 'Каталог Книг',
        'books': books,
    }
    return render(request, 'core/catalog.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    context = {
        'book': book,
    }
    return render(request, 'core/book_detail.html', context)

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('core:book_detail', pk=book.pk)
    else:
        form = BookForm()
    
    context = {
        'form': form,
        'title': 'Добавить книгу',
    }
    return render(request, 'core/book_form.html', context)

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('core:book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    
    context = {
        'form': form,
        'title': 'Редактировать книгу',
        'book': book,
    }
    return render(request, 'core/book_form.html', context)