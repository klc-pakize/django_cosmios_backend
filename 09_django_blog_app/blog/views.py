from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer
from .permissions import IsAdminOrReadOnly

class CategoryMVS(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name']
    search_fields = ["name"]
    permission_classes = [IsAdminOrReadOnly]


class BlogMVS(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_fields = ['category__name']
    search_fields = ["title", "content"]