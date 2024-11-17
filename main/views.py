from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from blog.models import Article
from portfolio.models import About, Education, Experience, ResearchInterests, Skill, Project, Certification, Reference
from .forms import SearchForm
def home_view(request):
    # Example of reversing both URLs
    portfolio_url = reverse('portfolio:about')  # Use 'portfolio' namespace
    articles_url = reverse('blog:blog')  # Use 'blog' namespace for articles
    return render(request, 'main/home.html', {
        'portfolio_url': portfolio_url,
        'articles_url': articles_url
    })

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:contact_success')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'main/contact_success.html')


def search_view(request):
    query = request.GET.get('q')
    articles = Article.objects.search(query) if query else []
    abouts = About.objects.filter(name__icontains=query) if query else []
    educations = Education.objects.filter(degree__icontains=query) if query else []
    experiences = Experience.objects.filter(title__icontains=query) if query else []
    skills = Skill.objects.filter(name__icontains=query) if query else []
    projects = Project.objects.filter(title__icontains=query) if query else []
    certifications = Certification.objects.filter(title__icontains=query) if query else []
    references = Reference.objects.filter(name__icontains=query) if query else []

    context = {
        'query': query,
        'articles': articles,
        'abouts': abouts,
        'educations': educations,
        'experiences': experiences,
        'skills': skills,
        'projects': projects,
        'certifications': certifications,
        'references': references,
    }
    return render(request, 'main/search_results.html', context)






