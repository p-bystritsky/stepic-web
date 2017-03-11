from django import forms
from django.contrib.auth.models import User

from .models import Question, Answer

from .local_settings import *


class GenericForm(forms.Form):
    # def __init__(self, model, user, *args, **kwargs):
    def __init__(self, model, *args, **kwargs):
        self.model = model
        # self.user = user
        super(forms.Form, self).__init__(*args, **kwargs)

    def clean(self):
        # no checks for now
        if False:
            raise forms.ValidationError()
        return self.cleaned_data

    def save(self):
        # self.cleaned_data['author'] = self.user
        obj = self.model(**self.cleaned_data)
        obj.save()
        return obj


class AskForm(GenericForm):
    title = forms.CharField(max_length=TITLE_MAX_LENGTH)
    text = forms.CharField(widget=forms.Textarea)

    # def __init__(self, user, *args, **kwargs):
    #     super(self.__class__, self).__init__(Question, user, *args, **kwargs)
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(Question, *args, **kwargs)


class AnswerForm(GenericForm):
    text = forms.CharField(widget=forms.Textarea)

    # def __init__(self, question_id, user, *args, **kwargs):
    def __init__(self, question_id, *args, **kwargs):
        self.question_id = question_id
        # super(self.__class__, self).__init__(Answer, user, *args, **kwargs)
        super(self.__class__, self).__init__(Answer, *args, **kwargs)

    def save(self):
        self.cleaned_data['question_id'] = self.question_id
        return super(self.__class__, self).save()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, max_length=255)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, max_length=255)

    def save(self):
        obj = User.objects.create_user(**self.cleaned_data)
        obj.save()
        return obj

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data) < MIN_USERNAME_LENGTH:
            raise forms.ValidationError(
                'Minimum length of Username is %(num)s symbols',
                params={'num': MIN_USERNAME_LENGTH}
            )
        try:
            User.objects.get(username=data)
        except User.DoesNotExist:
            return data
        else:
            raise forms.ValidationError(
                'User already exists'
            )

    def clean_password(self):
        data = self.cleaned_data['password']
        if len(data) < MIN_PASSWORD_LENGTH:
            raise forms.ValidationError(
                'Minimum length of Password is %(num)s symbols',
                params={'num': MIN_PASSWORD_LENGTH}
            )
        return data
