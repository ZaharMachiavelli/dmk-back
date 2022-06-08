from unicodedata import name
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.conf import settings

AGREGATORS = [('Skillbox', 'Skillbox'), ('GeekBrains', 'GeekBrains'), ('Netology', 'Нетология'), ('Yandex', 'Яндекс Практикум'), ('Skillfactory', 'Skillfactory'), ('Coursera', 'Coursera'), ('Stepik', 'Stepik'),]


class User(AbstractUser):
    biography = models.CharField("Биография", max_length= 255, null=True, blank=True)
    favourites = models.ManyToManyField("Course", null=True, blank=True)
    presets = models.ManyToManyField("CourseChain", blank=True, null=True)

    REQUIRED_FIELDS = ['biography', 'email', 'favourites', 'first_name', 'last_name']

    def __str__(self):
        return self.username

class CourseChain(models.Model):
    first = models.ManyToManyField('Course', blank=True, verbose_name = "1 предмет", related_name = "ebat_moi_hui1")
    second= models.ManyToManyField('Course', blank=True,  verbose_name = "2 предмет", related_name = "first1")
    third = models.ManyToManyField('Course', blank=True,  verbose_name = "3 предмет", related_name = "second1")
    forth = models.ManyToManyField('Course', blank=True,  verbose_name = "4 предмет", related_name = "third1")
    fifth = models.ManyToManyField('Course', blank=True,  verbose_name = "5 предмет", related_name = "forth1")
    sixth = models.ManyToManyField('Course', blank=True,  verbose_name = "6 предмет", related_name = "fifth1")
    seventh = models.ManyToManyField('Course', blank=True,  verbose_name = "7 предмет", related_name = "sixth1")
    eigth = models.ManyToManyField('Course', blank=True,  verbose_name = "8 предмет", related_name = "seventh1")
    ninth = models.ManyToManyField('Course', blank=True,  verbose_name = "9 предмет", related_name = "eigth1")
    tenth = models.ManyToManyField('Course', blank=True,  verbose_name = "10 предмет", related_name = "ninth1")

    def __str__(self):
        return f"Цепочка {self.pk}"

    class Meta:
        verbose_name = 'Цепочка'
        verbose_name_plural = 'Цепочки'

class Statistic(models.Model):

    YEARS = [('2017', 2017), ('2018', 2018), ('2019', 2019), ('2020', 2020), ('2021', 2021)]

    programmer = models.IntegerField(verbose_name = 'Программист')
    web = models.IntegerField(verbose_name = 'Веб')
    erp = models.IntegerField(verbose_name = 'ERP')
    marketing = models.IntegerField(verbose_name = 'Интернет-маркетинг')
    manager  = models.IntegerField(verbose_name = 'Менеджер')
    sysadmin = models.IntegerField(verbose_name = 'Системный администратор')
    analyst = models.IntegerField(verbose_name = 'Аналитик')
    support = models.IntegerField(verbose_name = 'Техподдержка')
    sysengineer = models.IntegerField(verbose_name = 'Системный инженер')
    engineer = models.IntegerField(verbose_name = 'Инженер')
    mobile = models.IntegerField(verbose_name = 'Mobile - разработчик')
    designeer = models.IntegerField(verbose_name = 'UX/UI дизайнер')
    director = models.IntegerField(verbose_name = 'Руководитель')
    devops = models.IntegerField(verbose_name = 'Devops')
    specialist = models.IntegerField(verbose_name = 'IT-специалист')
    security = models.IntegerField(verbose_name = 'Инфбез')
    gamedev = models.IntegerField(verbose_name = 'Gamedev')
    admindb = models.IntegerField(verbose_name = 'Администратор БД')
    datascience = models.IntegerField(verbose_name = 'Datascience')
    sysproger = models.IntegerField(verbose_name = 'Системный программист')
    notit = models.IntegerField(verbose_name = 'Не IT')
    year = models.CharField(choices = YEARS, unique = True, max_length = 255, verbose_name="Год")

    def __str__(self):
        return f"Статистика за {self.get_year_display()}"

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Годовые статистики'

class ProfessionCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование категории", null=True, blank=True)
    tag = models.CharField(max_length=255, verbose_name="Тег категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

class ProfessionDetail(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование профессии", null=True, blank=True)
    tag = models.CharField(max_length=255, verbose_name="Тег", blank=True, null=True, unique=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    first = models.ManyToManyField('Course', blank=True, verbose_name = "1 предмет", related_name = "ebat_moi_hui")
    second= models.ManyToManyField('Course', blank=True,  verbose_name = "2 предмет", related_name = "first")
    third = models.ManyToManyField('Course', blank=True,  verbose_name = "3 предмет", related_name = "second")
    forth = models.ManyToManyField('Course', blank=True,  verbose_name = "4 предмет", related_name = "third")
    fifth = models.ManyToManyField('Course', blank=True,  verbose_name = "5 предмет", related_name = "forth")
    sixth = models.ManyToManyField('Course', blank=True,  verbose_name = "6 предмет", related_name = "fifth")
    seventh = models.ManyToManyField('Course', blank=True,  verbose_name = "7 предмет", related_name = "sixth")
    eigth = models.ManyToManyField('Course', blank=True,  verbose_name = "8 предмет", related_name = "seventh")
    ninth = models.ManyToManyField('Course', blank=True,  verbose_name = "9 предмет", related_name = "eigth")
    tenth = models.ManyToManyField('Course', blank=True,  verbose_name = "10 предмет", related_name = "ninth")
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class Agregator(models.Model):

    name = models.CharField(max_length=1024, verbose_name= "Название агрегатора", null=True, blank=True)
    link = models.CharField(max_length=1024, verbose_name= "Ссылка на сайт")
    description = models.TextField(verbose_name= "Описание агрегатора")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Агрегатор'
        verbose_name_plural = 'Агрегаторы'

class Course(models.Model):
    name = models.CharField(max_length=1024, verbose_name= "Название курса", null=True, blank=True)
    slug = models.SlugField(max_length=128, verbose_name= "Тег курса", unique=True)
    description = models.TextField(verbose_name= "Описание")
    link = models.CharField(max_length=1024, blank=True, null=True, verbose_name= "Ссылка на курс")
    image = models.ImageField(upload_to="", verbose_name = 'Изображение', null=True, blank = True)
    agregator = models.ForeignKey(Agregator, blank=True, null=True, on_delete=models.CASCADE, verbose_name= "Автор курса")
    profession = models.ManyToManyField(ProfessionDetail, blank=True, verbose_name="Связанная профессия")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def get_absolute_url(self):
        return f"/courses/${self.slug}/"

    def get_image(self):
        print(settings.MEDIA_URL)
        print(settings.MEDIA_ROOT)
        print(self.image.url)
        if self.image:
           return 'https://urfuservice.herokuapp.com' + self.image.url
        return '' 
    

class ProfessionSkills(models.Model):
    profession = models.OneToOneField(ProfessionDetail, on_delete=models.CASCADE, verbose_name="Профессия")
    languages= models.FloatField(verbose_name="Языки программирования")
    dbms = models.FloatField(verbose_name="СУБД")
    instruments = models.FloatField(verbose_name="Интсрументы разработчика")
    patterns = models.FloatField(verbose_name="Паттерны")
    os = models.FloatField(verbose_name="Операционные системы")
    api = models.FloatField(verbose_name="API")
    soft = models.FloatField(verbose_name="Soft skills")
    web = models.FloatField(verbose_name="Web-разработка")
    layout = models.FloatField(verbose_name="Верстка")
    mobile = models.FloatField(verbose_name="Мобильная разработка")
    desktop = models.FloatField(verbose_name="Desktop")
    asu = models.FloatField(verbose_name="АСУ/АСУ ТП")
    erp = models.FloatField(verbose_name="КИС")
    graphic = models.FloatField(verbose_name="Работа с графикой")
    cms = models.FloatField(verbose_name="CMS")
    agile = models.FloatField(verbose_name="Agile")
    virtualization = models.FloatField(verbose_name="Средства виртуализации")
    marketing = models.FloatField(verbose_name="Интернет-маркетинг")
    serverpo = models.FloatField(verbose_name="Серверное ПО")
    webs = models.FloatField(verbose_name="Сети")
    infrastructure = models.FloatField(verbose_name="Инфрастрактура ПО")
    userpc = models.FloatField(verbose_name="Пользователь ПК")
    web_app = models.FloatField(verbose_name="Веб-приложения")
    testing = models.FloatField(verbose_name="Тестирование")
    standarts = models.FloatField(verbose_name="Стандарты")
    buisiness = models.FloatField(verbose_name="Бизнес-анализ")
    bigdata = models.FloatField(verbose_name="Big Data")
    web_services = models.FloatField(verbose_name="Web-сервисы")
    service = models.FloatField(verbose_name="Обслуживание")
    ml = models.FloatField(verbose_name="ML")
    gamedev = models.FloatField(verbose_name="GameDev")
    security = models.FloatField(verbose_name="Информационная безопасность")

    def __str__(self):
        return f"{self.profession.name} Навыки"

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"


# Create your models here.
