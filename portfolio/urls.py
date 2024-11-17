from django.urls import path, include
from .views import (
    AboutView,
    EducationView,
    SkillsView,
    ProjectCreateView,  # Ensure this is defined
    ProjectUpdateView,
    CertificationsView,
    ResearchInterestsView,
    ProjectListView,
    ProjectDetailView,
    ReferencesView,
    ExperienceView
)

app_name = 'portfolio'

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('education/', EducationView.as_view(), name='education'),
    path('skills/', SkillsView.as_view(), name='skills'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/update/<slug:slug>/', ProjectUpdateView.as_view(), name='project_update'),
    path('certifications/', CertificationsView.as_view(), name='certifications'),
    path('research/', ResearchInterestsView.as_view(), name='research'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('references/', ReferencesView.as_view(), name='references'),
    path('experience/', ExperienceView.as_view(), name='experience'),
]
