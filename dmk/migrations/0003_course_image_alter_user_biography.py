# Generated by Django 4.0.4 on 2022-06-01 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmk', '0002_rename_description_user_biography_user_favourites_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='user',
            name='biography',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Биография'),
        ),
    ]
