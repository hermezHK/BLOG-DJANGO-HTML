# Generated by Django 5.1 on 2024-08-28 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='actualizado',
        ),
    ]
