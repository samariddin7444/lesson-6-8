# Generated by Django 5.0.3 on 2024-04-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='media/book/'),
        ),
    ]
