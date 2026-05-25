from django import forms
from .models import Book, Comment

class FeedbackForm(forms.Form):
    subject = forms.CharField(
        max_length=250,
        label="Тема",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите тему'})
    )
    
    email = forms.EmailField(
        label="Ваш Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.ru'})
    )
    
    text = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Введите ваше сообщение'})
    )
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'publish_year', 'description', 'price', 'image', 'tags']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'publish_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 4, 'placeholder': 'Напишите ваш комментарий...'
            }),
        }
        labels = {
            'text': 'Ваш комментарий',
        }