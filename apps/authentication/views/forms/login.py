from django import forms


class LoginForm(forms.Form):
    attrs = {
        'class': 'form-control rounded-3',
        'placeholder': 'Something Random'
    }
    email = forms.EmailField(widget=forms.TextInput(attrs=attrs), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs), required=False)
