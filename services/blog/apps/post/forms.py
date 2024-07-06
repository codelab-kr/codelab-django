from django import forms

from . import models


class CreatePost(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = '__all__'  # ['title', 'image', 'body']
        labels = {
            'body': 'Caption',
        }
        widgets = {
            'body':
            forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Add a caption',
                    'class': 'font1 text-4xl',
                }),
        }
