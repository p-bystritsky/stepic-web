from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user, logout as logout_user

from .forms import AskForm, AnswerForm, LoginForm, SignUpForm
from models import Question, Answer

DEFAULT_PAGE_VALUE = 1
DEFAULT_LIMIT_VALUE = 10
INVALID_AUTH_MESSAGE = 'Invalid login or password'


@require_GET
def base(request, view):
    try:
        page = int(request.GET.get('page', DEFAULT_PAGE_VALUE))
        assert 0 < page
    except:
        page = DEFAULT_PAGE_VALUE
    try:
        limit = int(request.GET.get('limit', DEFAULT_LIMIT_VALUE))
        assert 0 < limit <= DEFAULT_LIMIT_VALUE
    except:
        limit = DEFAULT_LIMIT_VALUE
    paginator = Paginator(getattr(Question.objects, view)(), limit)
    paginator.baseurl = '%s?limit=%d&page=' % (reverse('qa:%s' % view), limit)
    page = paginator.page(min(page, paginator.num_pages))
    context = {
        'page': page,
        'questions': page.object_list,
        'paginator': paginator
    }
    return render(request, 'qa/%s.html' % view, context)


@require_GET
def new(request):
    return base(request, 'new')


@require_GET
def popular(request):
    return base(request, 'popular')


# @login_required
def view_question(request, q_id):
    question = get_object_or_404(Question, id=q_id)
    if not question.active:
        raise Http404()
    if request.method == 'POST':
        # form = AnswerForm(q_id, request.user, request.POST)
        form = AnswerForm(q_id, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        # form = AnswerForm(q_id, request.user)
        form = AnswerForm(q_id)
    answers = Answer.objects.filter(question=question)
    context = {
        'question': question,
        'answers': answers,
        'form': form
    }
    return render(request, 'qa/question.html', context)


# @login_required
def ask(request):
    if request.method == 'POST':
        # form = AskForm(request.user, request.POST)
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        # form = AskForm(request.user)
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=request.POST.get('username', None),
                password=request.POST.get('password', None),
            )
            if user is not None:
                login_user(request, user)
                next_page = request.GET.get('next', '/')
                return HttpResponseRedirect(next_page)
        form.add_error(None, INVALID_AUTH_MESSAGE)
    else:
        form = LoginForm()
    return render(request, 'qa/login.html', {'form': form})


@login_required
def logout(request):
    logout_user(request)
    next_page = request.GET.get('next', '/')
    return HttpResponseRedirect(next_page)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_user(request, user)
            next_page = request.GET.get('next', '/')
            return HttpResponseRedirect(next_page)
    else:
        form = SignUpForm()
    return render(request, 'qa/login.html', {'form': form})


def test(request, *args, **kwargs):
    return HttpResponse('OK')
