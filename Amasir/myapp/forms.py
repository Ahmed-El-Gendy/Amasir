from .models import Product, Customer, Order, OrderItem, Payment, Review
from django import forms

class CustomerSignUpForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        weidgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name', 'required': 'required', 'autofocus': 'autofocus', 'autocomplete': 'off'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email', 'required': 'required', 'autocomplete': 'off'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off'}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password', 'required': 'required', 'autocomplete': 'off'}),
            'is_admin': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'flexCheckDefault'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number', 'required': 'required', 'autocomplete': 'off'}),
        }
class CustomerLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
