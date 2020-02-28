from django.shortcuts import render
from catalog.models import Book, BookInstance, Author, Genre

def index(request):
    """View function for site homepage"""

    # generates counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books
    num_instances_available = BookInstance.objects.all().count()

    num_authors = Author.objects.count()

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


