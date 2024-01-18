from django. urls import path
from rest_framework. routers import DefaultRouter
from .views import BooksModelViewset
router = DefaultRouter
router.register(prefix:r'',BooksModelViewset,basename='books')
urlpatterns = [

] + router. urls
