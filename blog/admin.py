from django.contrib import admin
from .models import Author, Post, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    list_filter = ['date', 'tags']
    search_fields = ['title', 'content']
    readonly_fields = ['slug']


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
