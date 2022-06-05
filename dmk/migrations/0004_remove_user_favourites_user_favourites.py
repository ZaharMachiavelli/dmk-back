# Generated by Django 4.0.4 on 2022-06-04 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmk', '0003_course_image_alter_user_biography'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favourites',
        ),
        migrations.AddField(
            model_name='user',
            name='favourites',
            field=models.ManyToManyField(blank=True, null=True, to='dmk.course'),
        ),
    ]