from django.shortcuts import render, redirect
from . models import Post
from . form import PostForm
# Create your views here.

def homepage(request):
    return render(request, 'posts/index.html')

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    return render(request, 'posts/post_list.html', context)

def post_view(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        "post" : post
    }
    return render(request, 'posts/post_view.html', context)

def create_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/posts")

    context = {
        "form" : form
    }
    return render(request, 'posts/post_form.html', context)

def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(request.POST or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/posts')
    
    context = {
        "form" : form 
    }
    return render(request, 'posts/post_form.html', context)

def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('/posts')
    return render(request, 'posts/delete_post.html')
