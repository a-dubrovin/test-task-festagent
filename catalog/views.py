## -*- coding: utf-8 -*-
# Create your views here.

from django.views.generic import ListView
from catalog.models import Catalog
from catalog.helpers import generate_records

class CatalogList(ListView):
    model = Catalog

    def get(self, request, *args, **kwargs):
        if 'generate' in request.GET:
            generate_records(20)
        return super(CatalogList, self).get(request, *args, **kwargs)
