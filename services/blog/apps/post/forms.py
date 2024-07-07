from django import forms

from . import models

# from services.blog.apps.post.data import BOOK_CHOICES


class PostForm(forms.ModelForm):
    # book = forms.ChoiceField(choices=BOOK_CHOICES, label='책')
    # chapter_verse = forms.CharField(max_length=255, required=True, label='장/절')

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
