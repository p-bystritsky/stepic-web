from django import forms

from .models import Question, Answer

from .local_settings import *


class GenericForm(forms.Form):
    def __init__(self, model, user, *args, **kwargs):
        self.model = model
        self.user = user
        super(forms.Form, self).__init__(*args, **kwargs)

    def save(self):
        self.cleaned_data['author'] = self.user
        obj = self.model(**self.cleaned_data)
        obj.save()
        return obj


class AskForm(GenericForm):
    title = forms.CharField(max_length=TITLE_MAX_LENGTH)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, user, *args, **kwargs):
        super(self.__class__, self).__init__(Question, user, *args, **kwargs)

    def clean(self):
        # no checks for now
        if False:
            raise forms.ValidationError()
        return self.cleaned_data


class AnswerForm(GenericForm):
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, question_id, user, *args, **kwargs):
        self.question_id = question_id
        super(self.__class__, self).__init__(Answer, user, *args, **kwargs)

    def save(self):
        self.cleaned_data['question_id'] = self.question_id
        return super(self.__class__, self).save()
