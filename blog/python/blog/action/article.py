#!/usr/bin/env python
# -*- coding:utf-8 -*-

from blog.table.article import get_articles

class ArticleMgm(object):
    def __init__(self):
        pass
    
    test_result = [
            dict(
                title="Vital Films presents INSIGHT",
                abstract="Art and design have always been related, but today, experimentation and personal expression are the name of the game. Homeowners are using art to make a personal statement – your art choice has ...",
                blocks=[
                    "Design",
                    "Typography",
                    "Illustrations"
                ]
            ),
            dict(
                title="Vital Films presents INSIGHT",
                abstract="Art and design have always been related, but today, experimentation and personal expression are the name of the game. Homeowners are using art to make a personal statement – your art choice has ...",
                blocks=[
                    "Design",
                    "Typography",
                    "Illustrations"
                ]
            ),
            dict(
                title="Vital Films presents INSIGHT",
                abstract="Art and design have always been related, but today, experimentation and personal expression are the name of the game. Homeowners are using art to make a personal statement – your art choice has ...",
                blocks=[
                    "Design",
                    "Typography",
                    "Illustrations"
                ]
            ),
            dict(
                title="Vital Films presents INSIGHT",
                abstract="Art and design have always been related, but today, experimentation and personal expression are the name of the game. Homeowners are using art to make a personal statement – your art choice has ...",
                blocks=[
                    "Design",
                    "Typography",
                    "Illustrations"
                ]
            ),
            dict(
                title="Vital Films presents INSIGHT",
                abstract="Art and design have always been related, but today, experimentation and personal expression are the name of the game. Homeowners are using art to make a personal statement – your art choice has ...",
                blocks=[
                    "Design",
                    "Typography",
                    "Illustrations"
                ]
            ),
            dict(
                title="Vital Films presents INSIGHT",
                abstract="Art and design have always been related, but today, experimentation and personal expression are the name of the game. Homeowners are using art to make a personal statement – your art choice has ...",
                blocks=[
                    "Design",
                    "Typography",
                    "Illustrations"
                ]
            )
        ]

    # public stuffs

    def get_all_articles(self):
        # todo for test
        # return self.test_result
        all_articles = get_articles()
        return all_articles