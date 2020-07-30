from django.db import models

# Create your models here.


class Organization(models.Model):
    class Meta:
        verbose_name = 'Организация'

    name = models.CharField(verbose_name='Название организации', max_length=150, null=False, blank=False)
    bin = models.BigIntegerField(verbose_name='БИН', blank=False, null=False, unique=True)
    oked = models.BigIntegerField(verbose_name='ОКЭД', blank=False, null=False, unique=False)
    okpo = models.BigIntegerField(verbose_name='ОКПО', blank=False, null=False, unique=False)
    address = models.CharField(verbose_name='Юридический адрес', blank=True, null=True, max_length=150)
    owner = models.CharField(verbose_name='Руководитель', blank=True, null=True, max_length=150)
    created = models.DateField(verbose_name='Время открытия', blank=True, null=True)

    def __str__(self):
        return f'Организация - {self.name}'
