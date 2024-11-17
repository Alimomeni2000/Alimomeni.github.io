# mains/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


    