# Generated by Django 3.0.5 on 2023-10-09 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_add_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='url',
        ),
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
    ]
