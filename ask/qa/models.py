from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class QuestionManager(models.Manager):
    def __get_by(self, param, max_number=10, reverse=False):
        if reverse:
            param = '-' + param
        result = super(QuestionManager, self).get_queryset().order_by(param).all()
        return result[:min(max_number, result.count())]

    def new(self, max_number=10):
        return self.__get_by('added_at', max_number)


    def popular(self, max_number=10):
        return self.__get_by('rating', max_number)

class Entry(models.Model):
    text = models.TextField()
    added_at = models.DateField(default=datetime.now)
    author = models.ForeignKey(User)


class Question(Entry):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    likes = models.ManyToManyField(User)

    def __str__(self):
        return "Question #%d" % self.id


class Answer(Entry):
    question = models.ForeignKey(Question)

    def __str__(self):
        return "Answer #%d" % self.id

