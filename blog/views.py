from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from blog.models import Author, Post, Tag, Comment
from django.template.defaultfilters import slugify
from datetime import datetime
from django.views.generic import ListView, DetailView, View
from django.urls import reverse
from .forms import CommentForm, LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User




# Create your views here.


blog_data = [
    {
        "id": 1,
        "title": "Understanding Flexbox: A Comprehensive Guide",
        "author": "Jane Doe",
        "date": "2024-10-01",
        "summary": "This guide provides a deep dive into CSS Flexbox, covering everything from basic concepts to advanced layout techniques.",
        "tags": ["CSS", "Flexbox", "Web Development"],
        "slug": "understanding-flexbox-a-comprehensive-guide",
        "content":"""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"""
    },
    {
        "id": 2,
        "title": "React vs Vue: Choosing the Right Framework",
        "author": "John Smith",
        "date": "2024-09-28",
        "summary": "A comparison between React and Vue, exploring their strengths and weaknesses to help you choose the right framework for your next project.",
        "tags": ["JavaScript", "React", "Vue", "Frontend"],
        "slug": "react-vs-vue-choosing-the-right-framework",
        "content":"""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"""
    },
    {
        "id": 3,
        "title": "Boosting Performance in JavaScript Applications",
        "author": "Emily Johnson",
        "date": "2024-09-20",
        "summary": "Learn tips and techniques for optimizing the performance of JavaScript applications, including code splitting and lazy loading.",
        "tags": ["JavaScript", "Performance", "Optimization"],
        "slug": "boosting-performance-in-javascript-applications",
        "content":"""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"""
    },
    {
        "id": 4,
        "title": "An Introduction to RESTful APIs",
        "author": "Michael Brown",
        "date": "2024-09-15",
        "summary": "An overview of RESTful APIs, covering basic concepts, design principles, and best practices for building scalable APIs.",
        "tags": ["API", "REST", "Backend", "Web Development"],
        "slug": "an-introduction-to-restful-apis",
        "content":"""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"""
    },
    {
        "id": 5,
        "title": "Exploring CSS Grid for Modern Layouts",
        "author": "Sophia Williams",
        "date": "2024-09-10",
        "summary": "CSS Grid has become the go-to solution for creating responsive and modern web layouts. This article walks you through its core features and usage.",
        "tags": ["CSS", "Grid", "Web Design"],
        "slug": "exploring-css-grid-for-modern-layouts",
        "content":"""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
         Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"""
    }
]

tags = ["Fresh Content", "Trending Now", "Hot Tips", "Cool Insights", "Latest Buzz"]


#? Login

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'blog/login.html', {'form':form})
    def post(self,request):
        form = LoginForm(request.POST)
        print('POST')
        if form.is_valid():
            print('VALID FORM!')
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username,password)
            user = authenticate(request, username=username, password=password)
            print(user.email)

            if user is not None:
                login(request, user)
                print(user.email)
                print(f'Authenticated: {request.user.is_authenticated}')
                all_posts = reverse('blog_posts')
                return HttpResponseRedirect(all_posts)
        else:
        
        
            return render(request, 'blog/login.html', {'form':form})
        return render(request, 'blog/login.html', {'form':form})


#? Sign Up Class View

class SignUpView(View):
    def get(self,request):
        form = SignUpForm()
        return render(request,'blog/sign-up.html', {'form':form})
    
    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email,password=password)
            
            return HttpResponseRedirect(reverse('login'))
        return render(request, 'blog/sign-up.html',{'form':form})

#? Logout Class View

class LogoutView(View):
    def post(self,request):
        logout(request)
        return HttpResponseRedirect('login')

#? Function and Class view INDEX

# def index(request):
   
#     latest_post = Post.objects.latest('date')
#     print(latest_post)
    
#     return render(request, 'blog/index.html', {'post':latest_post})

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post'

    def get_queryset(self):
        query = super().get_queryset().latest('date')
        return query
    
    def get_context_data(self, **kwargs):
        form = CommentForm()

        context = super().get_context_data(**kwargs)
        context['form'] = form
        query = self.get_queryset()
        context['comments'] = query.comments.all().order_by('-id')
        session_id_list = self.request.session.get('post_id')
        if session_id_list is not None:
            is_in_read_later = query.id in session_id_list
            context['is_in_read_later'] = is_in_read_later
        else:
            context['is_in_read_later'] = False

        return context
    
    
 #? Function and Class view ALL POSTS

# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, 'blog/posts.html', {'posts':all_posts})

class PostsView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = ['-date']

    


 #? Function and Class view DETAILED POST

# def post(request,slug):
#     # try:
#     #     post = Post.objects.get(slug=slug)
#     # except Post.DoesNotExist:
#     #     raise Http404()
#     post = get_object_or_404(Post, slug=slug)    
#     return render(request, 'blog/post.html', {'post':post})

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
            form = CommentForm()

            context = super().get_context_data(**kwargs)
            context['form'] = form
            object = self.object
            context['comments'] = object.comments.all().order_by('-id')
            session_id_list = self.request.session.get('post_id')
            if session_id_list is not None:
                is_in_read_later = object.id in session_id_list
                context['is_in_read_later'] = is_in_read_later
            else:
                context['is_in_read_later'] = False

            return context




class AddRemoveReadLaterView(View):
    def post(self,request):
        id = request.POST.get('post_id')
        is_index = request.POST.get('url') == 'home-page'
        current_post = Post.objects.get(pk=int(id))
        if 'post_id' not in request.session:
            print('Creating List')

            request.session['post_id'] = []
        if int(id) not in request.session['post_id']:
            request.session['post_id'].append(int(id))
        else:
            request.session['post_id'].remove(int(id))

        request.session.modified = True  # Mark the session as modified

        posts = request.session.get('post_id')
        print(posts)
        if is_index:
            home = reverse('home')
            return HttpResponseRedirect(home)
        else:
            post = reverse('single_post', args=[current_post.slug])
            return HttpResponseRedirect(post)


class ReadLaterView(View):
    def get(self,request):
        is_list = False
        post_list = []
        if 'post_id' in request.session and len(request.session['post_id']) > 0:
            is_list = True
            post_id_list = request.session.get('post_id')
            post_list = [Post.objects.get(pk=item) for item in post_id_list]
        return render(request,'blog/read-later-posts.html', {'post_list':post_list, 'is_list':is_list})
    def post(self,request):
        request.session.clear()
        return HttpResponseRedirect(reverse('read_later_posts'))




class PostCommentView(View):
    def post(self, request, id):
        is_index = request.POST.get('url') == 'home-page'
        current_post = Post.objects.get(pk=id)
        comment_text = request.POST.get('comment')
        username = request.POST.get('username')
        form = CommentForm(request.POST)
        if form.is_valid():
            # new_comment = Comment(comment=comment_text, username=username)
            # new_comment.post = current_post
            # new_comment.save()
            #? You can call form.save() to save all the data
            new_comment = form.save(commit=False) # this create an instance
            new_comment.post = current_post
            new_comment.save() 

            print(current_post.comments.all())

            if is_index:
                home = reverse('home')
                return HttpResponseRedirect(home)
            else:
                post = reverse('single_post', args=[current_post.slug])
                return HttpResponseRedirect(post)
        else:
            

            if is_index:
                
                return render(request, 'blog/index.html', {'form':form, 'post':current_post})
            else:
                return render(request, 'blog/post.html', {'form':form, 'post':current_post})