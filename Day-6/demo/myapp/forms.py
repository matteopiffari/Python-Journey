from django import forms

class CreateNewItem(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    description = forms.CharField(label="Description", widget=forms.Textarea)