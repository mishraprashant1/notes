from django import forms


class CreateNewNoteForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15'}))
