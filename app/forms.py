from django import forms

from app.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'sub_title', 'post_image', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'My title'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'My Sub title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'My text here'}),
        }
