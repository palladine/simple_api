from django.contrib import admin
from api.models import Book, Author

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'year')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)