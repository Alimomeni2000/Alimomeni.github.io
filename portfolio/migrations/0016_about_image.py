# Generated by Django 5.1.2 on 2024-10-22 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_about_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='about_images/'),
        ),
    ]
