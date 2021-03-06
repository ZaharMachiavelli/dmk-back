# Generated by Django 4.0.4 on 2022-05-21 02:19

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agregator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Название агрегатора')),
                ('link', models.CharField(max_length=1024, verbose_name='Ссылка на сайт')),
                ('description', models.TextField(verbose_name='Описание агрегатора')),
            ],
            options={
                'verbose_name': 'Агрегатор',
                'verbose_name_plural': 'Агрегаторы',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Название курса')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='Тег курса')),
                ('description', models.TextField(verbose_name='Описание')),
                ('link', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Ссылка на курс')),
                ('agregator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dmk.agregator', verbose_name='Автор курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='ProfessionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование категории')),
                ('tag', models.CharField(max_length=255, verbose_name='Тег категории')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ProfessionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование профессии')),
                ('tag', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Тег')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('eigth', models.ManyToManyField(blank=True, related_name='seventh', to='dmk.course', verbose_name='8 предмет')),
                ('fifth', models.ManyToManyField(blank=True, related_name='forth', to='dmk.course', verbose_name='5 предмет')),
                ('first', models.ManyToManyField(blank=True, related_name='ebat_moi_hui', to='dmk.course', verbose_name='1 предмет')),
                ('forth', models.ManyToManyField(blank=True, related_name='third', to='dmk.course', verbose_name='4 предмет')),
                ('ninth', models.ManyToManyField(blank=True, related_name='eigth', to='dmk.course', verbose_name='9 предмет')),
                ('second', models.ManyToManyField(blank=True, related_name='first', to='dmk.course', verbose_name='2 предмет')),
                ('seventh', models.ManyToManyField(blank=True, related_name='sixth', to='dmk.course', verbose_name='7 предмет')),
                ('sixth', models.ManyToManyField(blank=True, related_name='fifth', to='dmk.course', verbose_name='6 предмет')),
                ('tenth', models.ManyToManyField(blank=True, related_name='ninth', to='dmk.course', verbose_name='10 предмет')),
                ('third', models.ManyToManyField(blank=True, related_name='second', to='dmk.course', verbose_name='3 предмет')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
            },
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programmer', models.IntegerField(verbose_name='Программист')),
                ('web', models.IntegerField(verbose_name='Веб')),
                ('erp', models.IntegerField(verbose_name='ERP')),
                ('marketing', models.IntegerField(verbose_name='Интернет-маркетинг')),
                ('manager', models.IntegerField(verbose_name='Менеджер')),
                ('sysadmin', models.IntegerField(verbose_name='Системный администратор')),
                ('analyst', models.IntegerField(verbose_name='Аналитик')),
                ('support', models.IntegerField(verbose_name='Техподдержка')),
                ('sysengineer', models.IntegerField(verbose_name='Системный инженер')),
                ('engineer', models.IntegerField(verbose_name='Инженер')),
                ('mobile', models.IntegerField(verbose_name='Mobile - разработчик')),
                ('designeer', models.IntegerField(verbose_name='UX/UI дизайнер')),
                ('director', models.IntegerField(verbose_name='Руководитель')),
                ('devops', models.IntegerField(verbose_name='Devops')),
                ('specialist', models.IntegerField(verbose_name='IT-специалист')),
                ('security', models.IntegerField(verbose_name='Инфбез')),
                ('gamedev', models.IntegerField(verbose_name='Gamedev')),
                ('admindb', models.IntegerField(verbose_name='Администратор БД')),
                ('datascience', models.IntegerField(verbose_name='Datascience')),
                ('sysproger', models.IntegerField(verbose_name='Системный программист')),
                ('notit', models.IntegerField(verbose_name='Не IT')),
                ('year', models.CharField(choices=[('2017', 2017), ('2018', 2018), ('2019', 2019), ('2020', 2020), ('2021', 2021)], max_length=255, unique=True, verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Статистика',
                'verbose_name_plural': 'Годовые статистики',
            },
        ),
        migrations.CreateModel(
            name='ProfessionSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.FloatField(verbose_name='Языки программирования')),
                ('dbms', models.FloatField(verbose_name='СУБД')),
                ('instruments', models.FloatField(verbose_name='Интсрументы разработчика')),
                ('patterns', models.FloatField(verbose_name='Паттерны')),
                ('os', models.FloatField(verbose_name='Операционные системы')),
                ('api', models.FloatField(verbose_name='API')),
                ('soft', models.FloatField(verbose_name='Soft skills')),
                ('web', models.FloatField(verbose_name='Web-разработка')),
                ('layout', models.FloatField(verbose_name='Верстка')),
                ('mobile', models.FloatField(verbose_name='Мобильная разработка')),
                ('desktop', models.FloatField(verbose_name='Desktop')),
                ('asu', models.FloatField(verbose_name='АСУ/АСУ ТП')),
                ('erp', models.FloatField(verbose_name='КИС')),
                ('graphic', models.FloatField(verbose_name='Работа с графикой')),
                ('cms', models.FloatField(verbose_name='CMS')),
                ('agile', models.FloatField(verbose_name='Agile')),
                ('virtualization', models.FloatField(verbose_name='Средства виртуализации')),
                ('marketing', models.FloatField(verbose_name='Интернет-маркетинг')),
                ('serverpo', models.FloatField(verbose_name='Серверное ПО')),
                ('webs', models.FloatField(verbose_name='Сети')),
                ('infrastructure', models.FloatField(verbose_name='Инфрастрактура ПО')),
                ('userpc', models.FloatField(verbose_name='Пользователь ПК')),
                ('web_app', models.FloatField(verbose_name='Веб-приложения')),
                ('testing', models.FloatField(verbose_name='Тестирование')),
                ('standarts', models.FloatField(verbose_name='Стандарты')),
                ('buisiness', models.FloatField(verbose_name='Бизнес-анализ')),
                ('bigdata', models.FloatField(verbose_name='Big Data')),
                ('web_services', models.FloatField(verbose_name='Web-сервисы')),
                ('service', models.FloatField(verbose_name='Обслуживание')),
                ('ml', models.FloatField(verbose_name='ML')),
                ('gamedev', models.FloatField(verbose_name='GameDev')),
                ('security', models.FloatField(verbose_name='Информационная безопасность')),
                ('profession', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dmk.professiondetail', verbose_name='Профессия')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='profession',
            field=models.ManyToManyField(blank=True, to='dmk.professiondetail', verbose_name='Связанная профессия'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('description', models.CharField(blank=True, max_length=15, null=True, verbose_name='Тельчик')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
