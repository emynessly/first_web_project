from django import forms
from .models import Book

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
        fields = ['name', 'author', 'publish_year', 'description', 'price']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'publish_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }