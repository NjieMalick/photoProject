from django.contrib import admin

from .models import Author, Post

admin.site.register(Author)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author')
	search_fields = ('author',)

