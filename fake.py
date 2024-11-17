import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_website.settings")  # Adjust 'portfolio_website' to match your project name
django.setup()

from faker import Faker
from django.contrib.auth.models import User
from blog.models import Category, Article, Comment, IPAddress
import random
from django.utils import timezone

# Initialize Faker
fake = Faker()

# Step 1: Create Fake Categories
categories = []
for _ in range(5):  # Creates 5 categories
    category = Category.objects.create(
        title=fake.word(),
        slug=fake.slug(),
        status=True,  # Sets category status to active
        position=random.randint(1, 10),  # Random position for ordering
    )
    categories.append(category)  # Adds the new category to a list for later use

# Step 2: Create a Test User
user, created = User.objects.get_or_create(username="testuser", email="test@example.com")
if created:
    user.set_password("password")  # Sets a password if user is created
    user.save()

# Step 3: Generate Fake Articles
articles = []
for _ in range(20):  # Creates 20 articles
    article = Article.objects.create(
        title=fake.sentence(),
        content=fake.paragraph(nb_sentences=5),
        author=user,  # Assigns the article to the test user
        jpublish=timezone.now(),
        is_special=random.choice([True, False]),
        status=random.choice(["d", "p", "l", "b"]),  # Randomly assigns a status
        category=random.choice(categories),  # Randomly assigns a category
        slug=fake.slug(),
    )
    articles.append(article)  # Adds the article to a list for later use

# Step 4: Add Fake Comments
for article in articles:
    for _ in range(random.randint(0, 5)):  # 0 to 5 comments per article
        Comment.objects.create(
            article=article,
            name=fake.name(),
            email=fake.email(),
            message=fake.sentence(),
        )

# Step 5: Add Fake IP Addresses and Hits
for article in articles:
    for _ in range(random.randint(1, 10)):  # Random number of hits per article
        ip_address, created = IPAddress.objects.get_or_create(ip_address=fake.ipv4())
        article.hits.add(ip_address)

print("Fake data added successfully!")
