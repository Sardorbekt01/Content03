from django.shortcuts import render
from .serializers import BookSerializer
from .models import Books
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(('GET', "POST"))
def book(request):
    if request.method == "GET":
        post = Books.objects.all()
        serializer = BookSerializer(post, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        post = BookSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(post.data)