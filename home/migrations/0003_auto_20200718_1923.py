# Generated by Django 3.0.2 on 2020-07-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_books_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='Category',
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.CharField(default='books_school', max_length=50),
        ),
    ]
