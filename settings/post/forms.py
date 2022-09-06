from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(min_length=2, label='Name', widget=forms.TextInput(attrs={
        'placeholder': 'Введите ваше имя',
        'class': 'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите ваш имэйл',
        'class': 'form-control'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Сообщение',
        'class': 'form-control',
        'cols': 30,
        'rows': 9,
        'style': 'height: 12rem',
    }))
