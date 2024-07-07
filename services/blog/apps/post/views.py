import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods

from services.blog.apps.post.books import BOOK_CHOICES

from . import forms
from .models import Post


def book_autocomplete(request):
    term = request.GET.get('term', '').lower()
    results = [
        {
            'id': value,
            'text': display
        } for value, display in BOOK_CHOICES if term in display.lower() or term in value.lower()
    ]
    return JsonResponse(results, safe=False)


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post.html', {'posts': posts})


@require_http_methods(['GET', 'POST'])
def post_create(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            query = form.cleaned_data.get('query')

            if query:
                url = f'http://ibibles.net/quote.php?{query}'
                print(url)
                response = requests.get(url)

                if response.status_code == 200:
                    post.verse = response.text
                else:
                    post.verse = 'Verse not found'
            # post.author = request.user
            post.save()
            return redirect('post_list')
    form = forms.PostForm()
    return render(request, 'post/create.html', {'form': form})


def get_verse(request):
    book = request.GET.get('book')
    chapter_verse = request.GET.get('chapter_verse')
    query = f'kor-{book}/{chapter_verse}'

    url = f'http://ibibles.net/quote.php?{query}'
    response = requests.get(url)

    if response.status_code == 200:
        verse = response.text
    else:
        verse = 'Error: Unable to fetch data.'

    html = render_to_string('post/verse_preview.html', {'verse': verse})
    return HttpResponse(html)
