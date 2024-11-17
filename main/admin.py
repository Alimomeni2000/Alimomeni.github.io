# main/admin.py
from django.contrib import admin
from .models import Contact, SocialMedia

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')  # Display these fields in the admin list
    search_fields = ('name', 'email', 'subject')  # Add search capability for these fields
    list_filter = ('created_at',)  # Add filtering options for the created_at field
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')  # Mark fields as read-only

admin.site.register(Contact, ContactAdmin)



@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'icon')  # Display name, URL, and icon in the admin list
    search_fields = ('name',)  # Add search functionality by social media name
