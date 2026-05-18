from django import forms

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