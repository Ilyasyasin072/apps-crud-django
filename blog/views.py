from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# create data damy array
# posts = [
#     {
#         'author': 'CoreyMs',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'post_posted': 'August 12 1992',
#     },
# {
#         'author': 'CoreyMs',
#         'title': 'Blog Post 2',
#         'content': 'First post content',
#         'post_posted': 'August 12 1992',
#     }
# ]


# Mendefinisikan function Home
@login_required
def home(request):
    # return HttpResponse('<h1>hi</h1>')
    context = {
        # post data dami di atas
        'posts': Post.objects.all()
    }
    return render (request, 'blog/home.html', context)


# Mendefinisikan function About
@login_required
def about(request):
    return render (request, 'blog/about.html', {'title': 'about'})
