from django.views import View
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth import get_user_model

from posts.models import Post
from posts.forms import PostForm, SearchForm

User = get_user_model()

def posts_list_view(request):
    if request.user.is_authenticated and request.user.role == User.UserType.PERSON:
        posts = request.user.posts.all()
   
    else:
        posts = Post.objects.all()
        
    return render(request, 'posts/index.html', context={'posts':posts})


def post_detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_detail.html', context={'post':post})

class PostCreateView(View):

    def get(self, request):
        form = PostForm()
        return render(request, 'posts/post_create.html', context={'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(obj)
        return render(request, 'posts/post_create.html', context={'form': form})


class PostUpdateView(View):

    def get(self, request, id):
        if not request.user.is_authenticated or request.user.role == 'PERSON':
            return redirect(reverse('posts_list_url'))

        obj = get_object_or_404(Post, id=id)
        bound_form = PostForm(instance=obj)
        return render(request, 'posts/post_update.html', context={'form': bound_form,
                                                        Post.__name__.lower(): obj})

    def post(self, request, id):
        obj = get_object_or_404(Post, id=id)
        bound_form = PostForm(request.POST, instance=obj)
        if bound_form.is_valid():
            obj = bound_form.save()
            return redirect(obj)
        return render(request, 'posts/post_update.html', context={'form': bound_form,
                                                        Post.__name__.lower(): obj})                                      


class PostDeleteView(View):
    
    def get(self, request, id):
        if not request.user.is_authenticated or request.user.role == 'person':
            return redirect(reverse('posts_list_url'))

        obj = get_object_or_404(Post, id=id)
        return render(request, 'posts/post_delete.html', context={Post.__name__.lower(): obj})

    def post(self,request, id):
        obj = get_object_or_404(Post, id=id)
        obj.delete()
        return redirect(reverse('posts_list_url'))