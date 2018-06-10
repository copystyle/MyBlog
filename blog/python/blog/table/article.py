#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db import transaction
from blog.models import Article

def get_all_articles(**kwargs):
    # read dummy objects
    articles = Article.objects.all(**kwargs)
    return articles

def add_article(**kwargs):
    # create a dummy object, short transaction
    article = Article(**kwargs)
    article.save()
    return article