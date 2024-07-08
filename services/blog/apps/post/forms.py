from django import forms

from . import models


class PostForm(forms.ModelForm):
    image = forms.URLField(assume_scheme='http')  # type: ignore

    class Meta:
        model = models.Post
        fields = ['title', 'image', 'book', 'chapter_verse', 'body']
        labels = {
            'body': 'Caption',
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add a caption',
                'class': 'font1 text-4xl',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        book = cleaned_data.get('book')
        chapter_verse = cleaned_data.get('chapter_verse')

        if book and chapter_verse:
            query = f'kor-{book}/{chapter_verse}'
            cleaned_data['query'] = query

        return cleaned_data
