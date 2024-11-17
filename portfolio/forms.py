from django import forms
from .models import Project, Experience, About, Certification  # Import About and Certification models
from ckeditor.widgets import CKEditorWidget

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'slug', 'description', 'link', 'image']  # Include image field
        widgets = {
            'description': CKEditorWidget(),  # Rich text editor for description
        }

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'  # or specify the fields you want to include
        widgets = {
            'description': CKEditorWidget(),  # Use CKEditorWidget for the description field
        }

# Similarly, ensure your other forms are set up to use CKEditorWidget
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'  # or specify the fields you want to include
        widgets = {
            'description': CKEditorWidget(),  # Use CKEditorWidget for the description field
        }

class CertificationForm(forms.ModelForm):  # New form for Certification model
    class Meta:
        model = Certification
        fields = ['title', 'description', 'date_received', 'download_link']  # Include all relevant fields
        widgets = {
            'description': CKEditorWidget(),  # Rich text editor for description
        }
