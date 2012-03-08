from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    website = forms.URLField(label='Website', required=False)
    comment = forms.CharField(max_length=500, widget=forms.Textarea)