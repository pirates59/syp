from django.shortcuts import render, HttpResponse, redirect
from .models import Post,Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # Import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def create(request):
    return render(request, 'blog/Create.html')

def creat(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        
        # Check if username consists solely of numeric characters
        if uname.isdigit():
            error_message = "Username cannot consist solely of numbers."
            return render(request, 'blog/Home.html', {'error_message': error_message})
        
        # If username is valid, create the user
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        messages.success(request, f'Account created for {uname}!')
        return redirect('create-login')
    
    return render(request, 'blog/Home.html')

def loginPage(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create-profile')
        else:
            error_message = "Email or password is incorrect"

    return render(request, 'blog/Login.html', {'error_message': error_message})

def LogoutPage(request):
    logout(request)
    return redirect('create-login')

@login_required
def post(request):
    username = request.user.username
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'blog/post.html', {'username': username, 'profiles':profile})
 

@login_required
def profile(request):
    username = request.user.username
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'blog/profile.html', {'username': username, 'profiles':profile})


@login_required
def helpline(request):
    username = request.user.username
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'blog/helpline.html', {'username': username, 'profiles':profile})
 

@login_required
def feed(request):
    username = request.user.username
    profile = Profile.objects.filter(user=request.user)
    context = {
        'username': username,  
        'profiles': profile,
        'posts': Post.objects.all()
    }
    return render(request, 'blog/Feed.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/Feed.html'
    context_object_name= 'posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields= ['content']
    template_name = 'blog/post_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields= ['content']
    template_name = 'blog/post_update.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url='http://127.0.0.1:8000/create/feed'

    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False