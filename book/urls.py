from .views import book
from django.urls import path
from . import views

urlpatterns =[
    path("book/",views.book),
]

