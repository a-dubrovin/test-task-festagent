## -*- coding: utf-8 -*-

from django.contrib import admin
from catalog.models import Catalog

class CatalogAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(Catalog, CatalogAdmin)
