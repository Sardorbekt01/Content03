# Generated by Django 4.2.7 on 2024-01-20 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Kitob rasmi'),
        ),
        migrations.AlterModelTable(
            name='books',
            table=None,
        ),
    ]
