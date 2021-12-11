from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Column, Layout, Submit, Row

from .models import *


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        exclude = ['user']


class CreateUserForm(UserCreationForm):
    #helper = FormHelper()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # def __init__(self, *args, **kwrgs):
        #     super().__init__(*args, **kwrgs)
        #     self.helper = FormHelper()
        #     self.helper.form_method = 'post'
        #     self.helper.add_input(Submit('signup', 'Sign Up'))

        #     self.helper.layout = Layout(
        #         Row(
        #             Column('username'),
        #             Column('email'),
        #         ),
        #         'password1',
        #         'password2',
        #     )


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class ContactForm(ModelForm):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name',
    }))
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email',
    }))
    contact_message = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your Message',
        'rows': '20'
    }))

    class Meta:
        model = Contact
        fields = '__all__'
