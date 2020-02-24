from django.contrib import admin
from .models import Author, Book, BookInstance, Genre

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)


# admin.site.register(Book)
# admin.site.register(BookInstance)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Genre)
