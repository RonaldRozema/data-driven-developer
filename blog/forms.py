from django import forms

class CommentForm(forms.Form):
    
    content = forms.CharField(max_length=1000)


class SearchForm(forms.Form):

    search_string = forms.CharField(max_length=20)