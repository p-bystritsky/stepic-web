from django.contrib import admin
from models import Question, Answer


class EntryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'added_at', 'author', 'short_text', 'active')

    def short_text(self, obj):
        return obj.text[:80]

    def short_title(self, obj):
        return obj.title[:80]


class QuestionAdmin(EntryAdmin):
    list_display = list(EntryAdmin.list_display)
    list_display.insert(list_display.index('short_text'), 'short_title')
    list_display.append('rating')


class AnswerAdmin(EntryAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
