from django.shortcuts import render
from .serializers import productsSerializers
from .models import products
from rest_framework import status, permissions, generics, viewsets


# Create your views here.
class StudentCurd(viewsets.ViewSetMixin, generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = products.objects.all()
    serializer_class = productsSerializers
    # permission_classes = [permissions.AllowAny]

