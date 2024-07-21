from django.contrib import admin
from .models import Author, Tag, Post, Project, Comment, Review

# Customizing the Author admin view
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    search_fields = ['first_name', 'last_name', 'username', 'email']

# Customizing the Tag admin view
class TagAdmin(admin.ModelAdmin):
    list_display = ['caption']
    search_fields = ['caption']

# Customizing the Post admin view
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'published']
    list_filter = ['author', 'created_at', 'published', 'tag']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']

# Customizing the Project admin view
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'updated_at', 'published']
    list_filter = ['author', 'updated_at', 'published']
    search_fields = ['name', 'description', 'content']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-updated_at']

# Customizing the Comments admin view
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at', 'published']
    list_filter = ['post', 'user', 'created_at', 'published']
    search_fields = ['comment']

# Customizing the Reviews admin view
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'project', 'created_at', 'published']
    list_filter = ['project', 'user', 'created_at', 'published']
    search_fields = ['review']

# Registering models with the admin site
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Review, ReviewAdmin)