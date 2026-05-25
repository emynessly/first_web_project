from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .forms import FeedbackForm, BookForm, CommentForm

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

class CatalogListView(ListView):
    model = Book
    template_name = 'core/catalog.html'
    context_object_name = 'books'
    ordering = ['-publish_year']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог Книг'
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'core/book_detail.html'
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'core/book_form.html'
    success_url = reverse_lazy('core:catalog')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить книгу'
        return context
    
    def form_valid(self, form):
        form.instance.writer = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f'Книга "{form.instance.name}" успешно добавлена!')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при добавлении книги.')
        return super().form_invalid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'core/book_form.html'
    
    def test_func(self):
        """Только автор книги может еe редактировать"""
        book = self.get_object()
        if self.request.user.is_superuser:
            return True
        return book.writer == self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать книгу'
        return context
    
    def get_success_url(self):
        return reverse_lazy('core:book_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Книга "{form.instance.name}" успешно обновлена!')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при редактировании книги.')
        return super().form_invalid(form)
    
class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'core/book_confirm_delete.html'
    success_url = reverse_lazy('core:catalog')
    
    def test_func(self):
        """Только автор книги может еe удалить"""
        book = self.get_object()
        if not book.writer:
            return self.request.user.is_superuser
        return self.request.user == book.writer
    
    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        messages.success(request, f'Книга "{book.name}" успешно удалена!')
        return super().delete(request, *args, **kwargs)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно. Добро пожаловать!')
            return redirect('core:index')
        else:
            messages.error(request, 'Ошибка регистрации. Проверьте введенные данные.')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
        'title': 'Регистрация',
    }
    return render(request, 'core/register.html', context)

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            
            messages.success(request, 'Ваш комментарий опубликован.')
        else:
            messages.error(request, 'Ошибка при публикации комментария')
    
    return redirect('core:book_detail', pk=post.pk)