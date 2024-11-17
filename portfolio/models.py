from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Each category must have a unique name

    def __str__(self):
        return self.name
    
class SkillsCategory(models.Model):
    name = models.CharField(max_length=120, unique=True)  # Each category must have a unique name
    def __str__(self):
        return self.name
    
class ExperienceCategory(models.Model):
    name = models.CharField(max_length=120, unique=True)  # Each category must have a unique name
    def __str__(self):
        return self.name
    
class Thesis(models.Model):
    name = models.CharField(max_length=300,null=True, unique=True) 
    grade = models.CharField(max_length=300,null=True, unique=True) 
    def __str__(self):
        return self.name
class Advisors(models.Model):
    name = models.CharField(max_length=120, null=True,unique=True)
    link = models.URLField(null=True, blank=True)  # Ensure this is present
    def __str__(self):
        return self.name

class About(models.Model):
    name = models.CharField(max_length=100)
    bio = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='about_images/', null=True, blank=True)  # New field for image upload
    file = models.FileField(upload_to='about/files/', null=True, blank=True)  # Add FileField for file upload
    download_link = models.URLField(null=True, blank=True)  # Ensure this is present
    
    def short_description(self):
        return (self.bio[:50] + '...') if len(self.bio) > 50 else self.bio

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now, null=True, blank=True) 
    end_date = models.DateField(blank=True, null=True)
    city =  models.CharField(max_length=100, null=True, blank=True)
    cPGA = models.FloatField(default=0.0, null=True, blank=True)
    cGPALastLwo  = models.FloatField(null=True, blank=True)
    cGPASpecialized = models.FloatField(null=True, blank=True)
    advisors = models.ForeignKey(Advisors, on_delete=models.CASCADE, related_name="advisors", null=True, blank=True)  
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE, related_name="thesis", null=True, blank=True)  
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"

class ResearchInterests(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    company = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(default=timezone.now) 
    end_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(ExperienceCategory, on_delete=models.CASCADE, related_name="experience")  # ForeignKey to Category
    def short_description(self):
        return (self.description[:50] + '...') if len(self.description) > 50 else self.description

    def __str__(self):
        return self.title

class Skill(models.Model):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'

    SKILL_LEVEL_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=SKILL_LEVEL_CHOICES, default=BEGINNER)
    category = models.ForeignKey(SkillsCategory, on_delete=models.CASCADE, related_name="skills")

    def __str__(self):
        return f"{self.name} ({self.level})"


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = RichTextField(null=True, blank=True) 
    link = models.URLField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    def short_description(self):
        return (self.description[:50] + '...') if len(self.description) > 50 else self.description

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Certification(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(null=True, blank=True)
    date_received = models.DateField(default=timezone.now)
    download_link = models.URLField(null=True, blank=True) 
    def short_description(self):
        return (self.description[:50] + '...') if len(self.description) > 50 else self.description

    def __str__(self):
        return f"{self.title} - {self.date_received.strftime('%B %Y')}"  # Format as "Month Year"



class Reference(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    role = models.CharField(max_length=100,null=True, blank=True)


    def __str__(self):
        return f"{self.name}, {self.position}"

