## -*- coding: utf-8 -*-

import random
import time
import os

import pycountry
from catalog.models import Catalog
from project_tt.settings import PROJECT_ROOT

def generate_records(count=20):
    names = generate_names_list(20)
    for i in xrange(count):
        item = Catalog()
        item.name = names[i]
        item.country = get_country()
        item.date = get_date()
        item.save()

def generate_names_list(count=20):
    words_file = open(os.path.join(PROJECT_ROOT, 'words.txt'), 'r')
    words_list = []
    for word in words_file:
        words_list.append("%s%s" % (word[0].upper(), word[1:]))
    words_file.close()
    words_list_len = len(words_list)
    names = []
    for i in xrange(count):
        name = "%s %s %s" % (words_list[random.randint(0,words_list_len)], words_list[random.randint(0,words_list_len)], words_list[random.randint(0,words_list_len)])
        names.append(name)
    return names
    
def get_country():
    country_index = random.randint(0, len(pycountry.countries)-1)
    country = list(pycountry.countries)[country_index]
    return country.name
    
def get_date():
    start_date = "1/1/2000 1:01 AM"
    end_date = "1/1/2012 1:01 AM"
    format_date = '%m/%d/%Y %I:%M %p'
    
    start_time = time.mktime(time.strptime(start_date, format_date))
    end_time = time.mktime(time.strptime(end_date, format_date))

    random_time = start_time + random.random() * (end_time - start_time)    
    return time.strftime("%Y-%m-%d", time.localtime(random_time))    
