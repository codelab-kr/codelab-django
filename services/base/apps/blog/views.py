from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from . import forms
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/post.html', {'posts': posts})


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            # new_post.author = request.user
            new_post.save()
            return redirect('home')
    form = forms.CreatePost()
    return render(request, 'blog/create.html', {'form': form})
