# Generated by Django 2.2.4 on 2024-04-03 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_auto_20240403_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='books_authors_app.Book'),
        ),
    ]
