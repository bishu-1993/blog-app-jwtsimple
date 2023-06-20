from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .forms import PostForm
from .serializers import PostSerializer
from django.urls import reverse_lazy
from rest_framework import status

# def home(request):
#     return render(request,'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
class ArticleView(DetailView):
    model = Post
    template_name = 'article_details.html'

# class AddPostView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'add_post.html'
#     # fields = '__all__'
class AddPostView(APIView):
    permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'add_post.html', {'form': form})
    #
    # def post(self, request):
    #     form = PostForm(request.POST)
    #
    #     serializer = PostSerializer(data=request.data)
    #     print('valid form')
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         print('valid serializer')
    #         return Response(serializer.data, status=201)
    #     return render(request, 'home.html', {'form': form})

    def get(self, request):
        # Retrieve all blog posts
        blog_posts = Post.objects.all()
        serializer = PostSerializer(blog_posts, many=True)

        return Response(serializer.data)

    def post(self, request):
        # Create a new blog post
        # serializer = PostSerializer(data=request.data)
        serializer = PostSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    # fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')






