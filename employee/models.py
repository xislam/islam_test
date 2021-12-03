from django.db import models

GENDER = (
    ('Мусчина', 'Мусчина'),
    ('Женщина', 'Женщина')
)


class Employers(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамиоия")
    age = models.IntegerField(verbose_name="возраст")
    gender = models.CharField(max_length=30, choices=GENDER, verbose_name="Пол")
    department = models.ForeignKey('Department', verbose_name="Отдел",
                                   related_name='departments', on_delete=models.CASCADE)
    programming_lan = models.ForeignKey('ProgrammingLanguage',
                                        verbose_name="Язык программирования",
                                        on_delete=models.CASCADE, related_name='programming')

    def __str__(self):
        return self.name.__str__()

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    floor = models.IntegerField(verbose_name="Этаж")

    def __str__(self):
        return self.name.__str__()

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=40, verbose_name="Имя")

    def __str__(self):
        return self.name.__str__()

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Язык программирований'

