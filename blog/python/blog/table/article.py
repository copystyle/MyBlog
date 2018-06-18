#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db import transaction
from blog.models import Article

def get_articles(**kwargs):
    articles = Article.objects.all()
    return articles

def add_article(**kwargs):
    article = Article(**kwargs)
    article.save()
    return article

def get_articles_by_block():
    pass

def get_article(**kwargs):
    article = Article.object.filter(**kwargs).first()
    if article:
        return article
    else:
        # todo raise exception
        pass