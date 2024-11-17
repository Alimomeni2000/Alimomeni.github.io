from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import About, Education, SkillsCategory, Certification, ResearchInterests, Project, Reference, ExperienceCategory
from .forms import *  # Import the specific forms


class AboutView(View):
    def get(self, request):
        about = About.objects.first()
        research_interests_data = ResearchInterests.objects.all()
        form = AboutForm(instance=about)  # Use AboutForm
        return render(request, 'portfolio/about.html', {
            'about': about,
            'research_interests': research_interests_data,
            'form': form,  # Pass the form to the template
            'download_link': about.download_link if about else None
        })

    def post(self, request):
        about = About.objects.first()  # Get the existing About object
        form = AboutForm(request.POST, request.FILES, instance=about)  # Use AboutForm for POST
        if form.is_valid():
            form.save()
            return redirect('portfolio:about')  # Redirect to the about page after saving
        return render(request, 'portfolio/about.html', {
            'about': about,
            'form': form,  # Pass the form with errors
            'download_link': about.download_link if about else None
        })


class EducationView(View):
    def get(self, request):
        education = Education.objects.all().order_by('-start_date')
        return render(request, 'portfolio/education.html', {'education': education})


class SkillsView(View):
    def get(self, request):
        categories = SkillsCategory.objects.prefetch_related('skills').all()
        return render(request, 'portfolio/skills.html', {'categories': categories})


class CertificationsView(View):
    def get(self, request):
        form = CertificationForm()
        return render(request, 'portfolio/certifications.html', {'form': form})

    def post(self, request):
        form = CertificationForm(request.POST)  # Include request.FILES if needed for files
        if form.is_valid():
            form.save()
            return redirect('portfolio:certifications')  # Adjust as needed
        return render(request, 'portfolio/certifications.html', {'form': form})
    

class ProjectCreateView(View):
    def get(self, request):
        form = ProjectForm()
        return render(request, 'portfolio/project_form.html', {'form': form})

    def post(self, request):
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:project_list')  # Redirect to the project list after saving
        return render(request, 'portfolio/project_form.html', {'form': form})


class ResearchInterestsView(View):
    def get(self, request):
        research = ResearchInterests.objects.all()
        return render(request, 'portfolio/research.html', {'research': research})


class ProjectListView(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, 'portfolio/project_list.html', {'projects': projects})


class ProjectDetailView(View):
    def get(self, request, slug):
        project = get_object_or_404(Project, slug=slug)
        return render(request, 'portfolio/project_detail.html', {'project': project})


class ReferencesView(View):
    def get(self, request):
        references = Reference.objects.all()
        return render(request, 'portfolio/references.html', {'references': references})
class ExperienceView(View):
    def get(self, request):
        categories = ExperienceCategory.objects.prefetch_related('experience').all()
        form = ExperienceForm()  # Initialize the form
        return render(request, 'portfolio/experience.html', {
            'categories': categories,
            'form': form,  # Pass the form to the template
        })

    def post(self, request):
        form = ExperienceForm(request.POST, request.FILES)  # Handle form submission
        if form.is_valid():
            form.save()
            return redirect('portfolio:experience')  # Redirect to the experience page after saving
        categories = ExperienceCategory.objects.prefetch_related('experience').all()
        return render(request, 'portfolio/experience.html', {
            'categories': categories,
            'form': form,  # Pass the form with errors
        })


class ProjectUpdateView(View):
    def get(self, request, slug):
        project = get_object_or_404(Project, slug=slug)
        form = ProjectForm(instance=project)  # Pre-fill the form with the project instance
        return render(request, 'portfolio/project_form.html', {'form': form})

    def post(self, request, slug):
        project = get_object_or_404(Project, slug=slug)
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('portfolio:project_detail', slug=project.slug)
        return render(request, 'portfolio/project_form.html', {'form': form})
