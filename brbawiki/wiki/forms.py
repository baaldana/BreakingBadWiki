from django import forms

class SearchBar(forms.Form):
    search_string = forms.CharField(label='search_string', max_length=50)
