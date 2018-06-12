#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.template import loader, Context
from blog.action.article import ArticleMgm
from django.shortcuts import render


class ImagesHandler(View):
    def get(self, request):
        #t = loader.get_template('index.html')
        context = dict()
        context['articles'] = ArticleMgm().get_all_articles()

        #return t.render(articles)
        return render(request, "index.html", context=context)
