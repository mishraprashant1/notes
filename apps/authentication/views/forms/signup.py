from django import forms


class SignUpForm(forms.Form):
    attrs = {
        'class': 'form-control rounded-3',
        'placeholder': 'Something Random'
    }
    first_name = forms.CharField(widget=forms.TextInput(attrs=attrs), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs=attrs), required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs=attrs), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs), required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs=attrs), required=False)
