from django.contrib import admin
from .models import (About, Experience, Category, SkillsCategory, ExperienceCategory, Education,
                      ResearchInterests, Skill, Project, Certification, Reference, Thesis, Advisors)
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.urls import reverse
from django.utils.html import format_html

# Admin form to use CKEditor for Project description
class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),  # Use CKEditor for rich text
        }

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'image', 'download_link', 'view_on_site_badge')  # Add view_on_site_badge

    # Method to generate a badge-style link to the public webpage for the about section
    def view_on_site_badge(self, obj):
        url = reverse('portfolio:about')  # Assuming this is the view name
        return format_html('<a href="{}" target="_blank"><span style="background-color:#17a2b8;color:white;padding:4px 8px;border-radius:5px;">View</span></a>', url)

    view_on_site_badge.short_description = 'View on Site'

    
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'subject', 'institution', 'city', 'cPGA','view_on_site_badge')

    def view_on_site_badge(self, obj):
        url = reverse('portfolio:skills')  # Replace with your actual view and args
        return format_html('<a href="{}" target="_blank"><span style="background-color:#17a2b8;color:white;padding:4px 8px;border-radius:5px;">View</span></a>', url)

    view_on_site_badge.short_description = 'View on Site'  # Label of the column in the admin list

@admin.register(ResearchInterests)
class ResearchInterestsAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'category', 'view_on_site_badge')
    list_filter = ('category', 'level')  # Include category in the display

    def view_on_site_badge(self, obj):
        url = reverse('portfolio:skills')  # Replace with your actual view and args
        return format_html('<a href="{}" target="_blank"><span style="background-color:#17a2b8;color:white;padding:4px 8px;border-radius:5px;">View</span></a>', url)

    view_on_site_badge.short_description = 'View on Site'  # Label of the column in the admin list

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm  # Use custom form with CKEditor
    list_display = ('title', 'link', 'short_description', 'image', 'view_on_site_badge')  # Add view_on_site_badge

    # Method to generate a badge-style link to the public webpage for the project
    def view_on_site_badge(self, obj):
        url = reverse('portfolio:project_detail', args=[obj.slug])  # Replace with your actual view and args
        return format_html('<a href="{}" target="_blank"><span style="background-color:#17a2b8;color:white;padding:4px 8px;border-radius:5px;">View</span></a>', url)

    view_on_site_badge.short_description = 'View on Site'  # Label of the column in the admin list

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'date_received', 'download_link','view_on_site_badge')
    search_fields = ('title', 'short_description', 'date_received',)  # Optional: make the title searchable

    def view_on_site_badge(self, obj):
        url = reverse('portfolio:certifications')  # Replace with your actual view and args
        return format_html('<a href="{}" target="_blank"><span style="background-color:#17a2b8;color:white;padding:4px 8px;border-radius:5px;">View</span></a>', url)

    view_on_site_badge.short_description = 'View on Site'  # Label of the column in the admin list

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'contact','role', 'view_on_site_badge')

    def view_on_site_badge(self, obj):
        url = reverse('portfolio:references')  # Replace with your actual view and args
        return format_html('<a href="{}" target="_blank"><span style="background-color:#17a2b8;color:white;padding:4px 8px;border-radius:5px;">View</span></a>', url)

    view_on_site_badge.short_description = 'View on Site'  # Label of the column in the admin list

# Register the Category model
admin.site.register(Category)
admin.site.register(SkillsCategory)
admin.site.register(ExperienceCategory)
admin.site.register(Thesis)
admin.site.register(Advisors)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'category', 'view_on_site_badge')

    # Method to generate a badge-style link to the public webpage for the experience
    def view_on_site_badge(self, obj):
        url = reverse('portfolio:experience')  # Replace with your actual view and args
        return format_html('<a href="{}" target="_blank"><span style="background-color:#17a2b8;color:white;padding:4px 8px;border-radius:5px;">View</span></a>', url)

    view_on_site_badge.short_description = 'View on Site'