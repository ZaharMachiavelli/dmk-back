# Generated by Django 4.0.4 on 2022-06-08 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmk', '0005_alter_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image_link',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Хуйня'),
        ),
    ]
