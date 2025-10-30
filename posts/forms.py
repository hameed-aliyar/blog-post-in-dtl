from django import forms
from .models import Posts

class CreatePostForm(forms.ModelForm):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    class Meta:
        model = Posts
        fields = ['title', 'content']

class EditPostForm(forms.ModelForm):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    class Meta:
        model = Posts
        fields = ['title', 'content']