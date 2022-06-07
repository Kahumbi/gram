from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'gram/home.html', context)
    
class PostListView(ListView):
    model = Post
    template_name = 'gram/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] 
    
class PostDetailView(DetailView):
    model = Post   
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title','image',  'content']

def about(request):
    return render(request, 'gram/about.html', {'title':'About'})
    