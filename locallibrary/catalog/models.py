from django.db import models
from django.urls import reverse

class Genre(models.Model):
    """model representing a book's genre"""
    name = models.CharField(max_length=200, help_text='Enter a book genre (sci fi, kid lit, comics, etc)')

    def __str__(self):
        return self.name

class Book(models.Model):
    """ model representing a book, but not a specific copy of a book """
    title = models.CharField(max_length=200)

    # foreign key used so that it can be one author with multiple books, but not one book with multiple authors. This tutorial isn't ready to handle anthologies or Good Omens yet.
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # using a many to many field since books can have multiple genres and genres can have multiple books
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

class Author:
    pass

