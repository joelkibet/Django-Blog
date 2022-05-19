from django.shortcuts import render
from .models import Post

def homepage(request):
    return render(request, 'index.html', {"post": Post.objects.all})

# Create your views here.
