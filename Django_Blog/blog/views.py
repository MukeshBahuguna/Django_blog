from django.shortcuts import render,get_object_or_404  #shorter version
from django.http import HttpResponse
from .models import Post
from django.views.generic import (ListView,
                                    DetailView,
                                    CreateView,UpdateView,
                                    DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin                          
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    posts=Post.objects.all()

    context={'posts': posts}
    return render(request,'blog/home.html',context=context)

#class based views
#special feature

# things like ListView which are imported from django's set of libraries
#look for some specific things until we manually change there way of operating.  
# in class below what we didn't even needed template name and other stuff 
# if we created one new template and changed the name of the variable 

class PostListView(ListView):
    model =Post
    template_name='blog/home.html'
    context_object_name= 'posts'  # as we already made html using name 'posts' in it
    ordering=['date_posted']  # put '-' to reverse the order of the posts
    paginate_by=5

class UserPostListView(ListView):
    model =Post
    template_name='blog/user_posts.html'
    context_object_name= 'posts'  # as we already made html using name 'posts' in it
    paginate_by=5

    def get_queryset(self):  # for enabling that use link when you click on it it shows you post by specific user
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')


class PostDetailView(DetailView): #going to look for template called appname/modelname_detail(view).html that is ==> blog/post_detail.html
    model=Post
    

class PostCreateView(LoginRequiredMixin,CreateView):   #as these are classes we cannot put decorator instead what we do is import a class and inherit from it
    model=Post
    fields= [ 'title' , 'content']

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form) 

    #we can use success_url='blog-home' to redirect to home page

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):   #as these are classes we cannot put decorator instead what we do is import a class and inherit from it
    model=Post
    fields= [ 'title' , 'content']

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form) 


    def test_func(self):
        post=self.get_object()  # to get current post
        return self.request.user==post.author
        # return super().test_func()

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): 
    model=Post
    success_url='/'

    def test_func(self):
        post=self.get_object()  # to get current post
        return self.request.user==post.author

    

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})

