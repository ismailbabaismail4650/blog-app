from django.forms import BaseModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm,EditComment
from django.http import HttpResponse, HttpResponseRedirect

from .models import Post, Category, Comment

# Create your views here.
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked =True
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

class HomeView (ListView):
    model = Post
    template_name = "base/home.html"
    cats = Category.objects.all()
    ordering = ['-date_posted']
    
    def get_context_data (self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data()
        context ["cat_menu"] = cat_menu
        return context
        
    
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats) 
    return render (request,"base/category.html", {'cats':cats, 'category_posts':category_posts})

    
    


class PostDetailView (DetailView):
    model = Post
    template_name = "base/post_detail.html"

    def get_context_data (self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView,self).get_context_data()
        stuff  = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked= False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context ["cat_menu"] = cat_menu
        context ["total_likes"] = total_likes
        context ["liked"] = liked
        return context


class AddPostView (CreateView):
    model = Post
    form_class = PostForm
    template_name = "base/add_post.html"

    def get_context_data (self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data()
        context ["cat_menu"] = cat_menu
        return context
    

class AddCommentView (CreateView):
    model = Comment
    form_class = EditComment
    template_name = "base/comment.html"

    def form_valid(self, form):
        form.instance.post_id =self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')







class AddCategoryView (CreateView):
    model = Category
#    form_class = PostForm
    template_name = "base/add_category.html"
    fields = "__all__"

    def get_context_data (self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView,self).get_context_data()
        context ["cat_menu"] = cat_menu
        return context

class EditPostView (UpdateView):
    model = Post
    form_class = EditForm
    template_name = "base/update_post.html"

    def get_context_data (self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(EditPostView,self).get_context_data()
        context ["cat_menu"] = cat_menu
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = "base/delete.html"
    success_url = reverse_lazy('home')

    def get_context_data (self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView,self).get_context_data()
        context ["cat_menu"] = cat_menu
        return context
    


