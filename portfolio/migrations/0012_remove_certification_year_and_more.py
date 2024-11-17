# Generated by Django 5.1.2 on 2024-10-21 21:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_certification_download_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certification',
            name='year',
        ),
        migrations.AddField(
            model_name='certification',
            name='date_received',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
