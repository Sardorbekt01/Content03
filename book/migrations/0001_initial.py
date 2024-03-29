# Generated by Django 5.0.1 on 2024-01-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50, verbose_name='Kitob nomi')),
                ('book_author', models.CharField(max_length=5, verbose_name='Kitob muallifi')),
                ('book_price', models.IntegerField(verbose_name='Kitob narxi')),
                ('book_image', models.ImageField(upload_to='', verbose_name='Kitob rasmi')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
