#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.contrib import admin
from blog.models import Article, Block

admin.site.register(Article)
admin.site.register(Block)
