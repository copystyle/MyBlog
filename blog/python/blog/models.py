#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db import models


class Block(models.Model):
    """板块"""
    block_id = models.IntegerField("BlockId")
    name = models.CharField("BlockName", max_length=100)
    desc = models.CharField('BlockDesc', max_length=100)


class Article(models.Model):
    """文章"""
    article_id = models.IntegerField("ArticleId", primary_key=True)
    title = models.CharField("ArticleTitle", max_length=100)
    content = models.TextField("ArticleContent")
    abstract = models.TextField("ArticleAbstract", max_length=250)
    create_date = models.DateField("ArticleCreateDate")
    modify_date = models.DateField("ArticleModifyDate")
    reading_times = models.IntegerField("ReadingTimes")
    block_id = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='articles')
