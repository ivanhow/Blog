from django import forms

from app.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'sub_title', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'My title'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'My Sub title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'My text here'}),
        }
