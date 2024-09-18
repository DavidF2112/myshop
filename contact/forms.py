from django import forms
from .models import MessageFromCustomer, Subscriber


class MessageFromCustomerForm(forms.ModelForm):
    class Meta:
        model = MessageFromCustomer
        fields = ('name', 'email', 'subject', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-light border-0 px-4',
                                           'placeholder': 'Ваше Имя',
                                           'style': 'height: 55px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-light border-0 px-4',
                                             'placeholder': 'Ваш Email',
                                             'style': 'height: 55px;'}),
            'subject': forms.TextInput(attrs={'class': 'form-control  bg-light border-0 px-4',
                                              'placeholder': 'Обьект',
                                              'style': 'height: 55px;'}),
            'message': forms.Textarea(attrs={'class': 'form-control  bg-light border-0 px-4 py-3',
                                             'rows': '4',
                                             'placeholder': 'Сообщение'}),
        }


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control border-white p-3',
                                             'placeholder': 'Ваш Email'})
        }