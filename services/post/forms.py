from django import forms

from . import models


class PostForm(forms.ModelForm):
    image = forms.URLField(
        label='Image URL', widget=forms.URLInput(attrs={'placeholder': 'http://example.com/image.jpg'})
    )

    class Meta:
        model = models.Post
        fields = ['title', 'image', 'book', 'chapter_verse', 'body']
        labels = {
            'body': 'Caption',
        }
        widgets = {
            'body':
            forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add a caption',
                'class': 'font1 text-4xl rounded-md',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control rounded-md'})

    def clean(self):
        cleaned_data = super().clean()
        book = cleaned_data.get('book')
        chapter_verse = cleaned_data.get('chapter_verse')

        if book and chapter_verse:
            query = f'kor-{book}/{chapter_verse}'
            cleaned_data['query'] = query

        return cleaned_data
