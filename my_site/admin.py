from django.contrib import admin
from .models import Author, Tag

# Customizing the Author admin view
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    search_fields = ['first_name', 'last_name', 'username', 'email']

# Customizing the Tag admin view
class TagAdmin(admin.ModelAdmin):
    list_display = ['caption']
    search_fields = ['caption']

# Registering models with the admin site
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)