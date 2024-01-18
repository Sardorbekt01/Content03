from django.shortcuts import render
from .serializers import BookSerializer
from .models import Books
# Create your views here.
class BooksModelViewset():
    queryset = Books.objects.all()
    serializer_class = BookSerializer
