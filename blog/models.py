from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User 
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import Q
from ckeditor.fields import RichTextField  # Import RichTextField

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='IP Address')

    def __str__(self):
        return self.ip_address

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

    def search(self, query=None):
        """Search for articles by title, content, or category."""
        if query:
            return self.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(category__title__icontains=query)
            ).distinct()
        return self.published()  # Default to returning published articles

class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, default=None, on_delete=models.SET_NULL, related_name='children', verbose_name='Subcategory')
    title = models.CharField(max_length=200, verbose_name='Category Title')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Category Address')
    status = models.BooleanField(default=True, verbose_name='Is it displayed?')
    position = models.IntegerField(verbose_name='Position')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title

    objects = CategoryManager()

class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.article.title}"

class Article(models.Model):
    STATUS_CHOICES = (
        ("d", "Draft"),
        ("p", "Published"),
        ("l", "Checking"),
        ("b", "Returned"),
    )
    
    title = models.CharField(max_length=200)
    content = RichTextField()  # Change to RichTextField
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    jpublish = models.DateTimeField()
    is_special = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='Status')
    hits = models.ManyToManyField(IPAddress, through="ArticleHit", blank=True, related_name="hits", verbose_name="Hits")
    comments = GenericRelation(Comment)
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='articles/images/', null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def hit_count(self):
        return self.hits.count()
    
    def __str__(self):
        return self.title

    objects = ArticleManager()

class ArticleHit(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.article.title} - {self.ip_address.ip_address}"
