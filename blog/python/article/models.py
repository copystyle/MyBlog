#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db import models


class Article(models.Model):
    """文章"""
    id = models.IntegerField('ArticleId', primary_key=True)
    title = models.CharField('ArticleTitle', max_length=100)
    content = models.TextField('ArticleContent')
    date = models.DateField('ArticleDate')


class Block(models.Model):
    """板块"""
    name = models.CharField('板块名称', max_length=100)
    desc = models.CharField('板块描述', max_length=100)
    managerName = models.CharField('板块管理员名称', max_length=100)
    status = models.IntegerField('状态', choices=((0, '正常'), (-1, '删除')))
