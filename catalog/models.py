## -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Catalog(models.Model):
    name = models.CharField(max_length=10, verbose_name=u'Название')
    country = models.TextField(verbose_name=u'Страна')
    date = models.DateField(verbose_name=u'Дата начала')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = (u'Кинофестиваль')
        verbose_name_plural = (u'Кинофестивали')
        ordering = ('name',) 
