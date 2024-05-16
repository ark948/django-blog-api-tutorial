from rest_framework import generics, permissions
from posts.models import Post
from posts.serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,) # only admin users can view detail page
    queryset = Post.objects.all()
    serializer_class = PostSerializer