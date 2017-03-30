from django import forms

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit unsnazzed url')
