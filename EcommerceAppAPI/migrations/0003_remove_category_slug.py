# Generated by Django 5.0.6 on 2024-05-20 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceAppAPI', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
