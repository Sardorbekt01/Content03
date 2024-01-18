from django.db import models

class Books (models. Model):
    book_title = models. CharField(max_length=50, verbose_name= 'Kitob nomi')
    book_author = models.CharField(max_length=5, verbose_name='Kitob muallifi')
    book_price = models.IntegerField(verbose_name= 'Kitob narxi')
    book_image = models.ImageField(verbose_name= 'Kitob rasmi')
    def __str__(self) -> str:
        return f"{self.book_title}- {self.book_author}"
    class Meta:
        db_table = 'books'

