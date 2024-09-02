from django.contrib import admin
from .models import Post, Comment


# Customizing the Post admin view
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'published']
    list_filter = ['author', 'created_at', 'published', 'tag']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']

# Customizing the Comments admin view
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at', 'published']
    list_filter = ['post', 'user', 'created_at', 'published']
    search_fields = ['comment']


# Registering models with the admin site
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
