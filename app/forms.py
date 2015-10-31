from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length = 30)
    content = forms.CharField(widget = forms.Textarea, max_length = 140)
