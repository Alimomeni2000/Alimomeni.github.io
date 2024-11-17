from django.contrib import admin
from .models import Article, Category, IPAddress, ArticleHit, Comment
from django.utils.html import format_html

from django.contrib import admin
from django.utils.html import format_html
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'image_thumbnail', 'category', 'is_special', 'jpublish', 'status_badge', 'slug_url', 'delete_button')
    search_fields = ('title', 'content', 'author')
    list_filter = ('status', 'is_special', 'category')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'jpublish'
    ordering = ('-jpublish',)
    
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'content', 'category', 'image')
        }),
        ('Publication', {
            'fields': ('status', 'is_special', 'jpublish', 'slug'),
        }),
    )

    # Method to construct the article URL
    def slug_url(self, obj):
        article_url = f"/blog/{obj.slug}/"
        return format_html('<a href="{}">{}</a>', article_url, obj.slug)
    slug_url.short_description = 'Article URL'

    # Method for displaying status with badges
    def status_badge(self, obj):
        badge_color = {
            "p": "badge-success",
            "d": "badge-secondary",
            "l": "badge-warning",
            "b": "badge-danger"
        }.get(obj.status, "badge-light")
        return format_html('<span class="badge {}">{}</span>', badge_color, obj.get_status_display())
    status_badge.short_description = 'Status'

    # Method for displaying image thumbnails
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
        return "No Image"
    image_thumbnail.short_description = 'Thumbnail'

    # Add delete button for each row
    def delete_button(self, obj):
        return format_html(
            '<a href="/admin/{}/{}/{}/delete/" class="button" style="color: red;">Delete</a>',
            obj._meta.app_label,
            obj._meta.model_name,
            obj.id,
        )
    delete_button.short_description = 'Delete'

# Register other models
admin.site.register(Comment)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'position', 'parent')
    list_filter = ('status',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('position',)  # Ensure categories are listed in the correct order

@admin.register(IPAddress)
class IPAddressAdmin(admin.ModelAdmin):
    list_display = ('ip_address',)

@admin.register(ArticleHit)
class ArticleHitAdmin(admin.ModelAdmin):
    list_display = ('article', 'ip_address', 'created')
    search_fields = ('article__title',)
    list_filter = ('created',)  # Option to filter by date of hit
    ordering = ('-created',)  # Order hits by creation date

