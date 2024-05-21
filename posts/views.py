from rest_framework import viewsets
from posts.models import Post
from posts.serializers import PostSerializer, UserSerializer
from posts.permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer