from django.db import models
from ckeditor.fields import RichTextField

from .utilts import upload_to_common


class PersonalInfo(models.Model):
    fullname = models.CharField("Полное имя", max_length=255)
    profession = models.CharField("Профессия", max_length=255)
    image = models.ImageField("Картинка баннера", upload_to=upload_to_common, null=True)
    image_mobile = models.ImageField("Картинка баннера для мобилки", upload_to=upload_to_common, null=True)
    resume_file = models.FileField("Файл резюме", upload_to=upload_to_common, null=True, blank=True)
    about_me = RichTextField("Текст обо мне")
    linked_in = models.CharField("Ссылка на LinkedIn", max_length=255, default="")
    github = models.CharField("Ссылка на GitHub", max_length=255, default="")
    email = models.CharField("Почта", max_length=255, default="")
    phone_number = models.CharField("Номер телефона", max_length=255, default="")


    class Meta:
        verbose_name = "Персональная информация"
        verbose_name_plural = "Персональная информация"

    def __str__(self):
        return self.fullname

class AdditionalInfo(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="additional_info", null=True)
    icon = models.ImageField("Иконка", upload_to=upload_to_common)
    title = models.CharField("Заголовок", max_length=50)
    text = RichTextField("Текст")


    class Meta:
        verbose_name = "Дополнительная информация"
        verbose_name_plural = "Дополнительная информация"

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    text = RichTextField("Текст")

    class Meta:
        verbose_name = "Опыт"
        verbose_name_plural = "Опыт"

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    icon = models.ImageField("Иконка компании", upload_to=upload_to_common)
    company_name = models.CharField("Название компании", max_length=100)
    position = models.CharField("Позиция на работе", max_length=255)
    responsibility = RichTextField("Обязанности на работе")
    leadership = models.BooleanField("Лидерство", default=False)


    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"

    def __str__(self):
        return self.company_name


class Portfolio(models.Model):
    image = models.ImageField("Картинка", upload_to=upload_to_common)
    image_mobile = models.ImageField("Картинка для мобилки", upload_to=upload_to_common)
    project_name = models.CharField("Название проекта", max_length=255)
    github_link = models.CharField("Ссылка на гитхаб проекта", max_length=255, null=True, blank=True)
    live_demo = models.TextField("Ссылка на демо", null=True, blank=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.project_name


class ContactMe(models.Model):
    fullname = models.CharField("ФИО", max_length=255)
    email = models.EmailField("Почта", max_length=255)
    text = models.TextField("Текст")

    class Meta:
        verbose_name = "Связь"
        verbose_name_plural = "Связи"

    def __str__(self):
        return f"письмо от {self.fullname}"