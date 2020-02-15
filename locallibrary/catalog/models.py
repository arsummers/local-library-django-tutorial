from django.db import models

class Genre(models.Model):
    """model representing a book's genre"""
    name = models.CharField(max_length=200, help_text='Enter a book genre (sci fi, kid lit, comics, etc)')

    def __str__(self):
        return self.name

class Book:
    pass

class Author:
    pass

