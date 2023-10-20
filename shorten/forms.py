from django import forms

class IndexForm(forms.Form):
    long_url = forms.CharField(label='Long URL', max_length=200)