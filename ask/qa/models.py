from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .local_settings import *


class QuestionManager(models.Manager):
    def __get_by(self, param, reverse=False, only_active=True):
        if reverse:
            param = '-' + param
        result = Question.objects.all()
        if only_active:
            result = result.filter(active=True)
        return result.order_by(param)

    def new(self):
        return self.__get_by('added_at', reverse=True)

    def popular(self):
        return self.__get_by('rating', reverse=True)


class Entry(models.Model):
    text = models.TextField()
    added_at = models.DateField(default=datetime.now)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Question(Entry):
    objects = QuestionManager()

    author = models.ForeignKey(User)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    rating = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, blank=True, null=True, related_name='likes_user')

    def __str__(self):
        return "Question #%d" % self.id

    def get_url(self):
        return reverse('qa:question', kwargs={'q_id': self.pk})


class Answer(Entry):
    author = models.ForeignKey(User)
    question = models.ForeignKey(Question)

    def __str__(self):
        return "Answer #%d" % self.id
