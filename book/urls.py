from .views import BooksModelViewset
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books',BooksModelViewset,basename=-"books")
urlpatteras = router.urls
