from django.contrib import admin
from .models import Author, Post, Tag, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    list_filter = ['date', 'tags']
    search_fields = ['title', 'content']
    readonly_fields = ['slug']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_email', 'text', 'post']


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
