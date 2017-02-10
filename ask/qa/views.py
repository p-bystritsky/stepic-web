from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET

from models import Question, Answer

DEFAULT_PAGE_VALUE = 1
DEFAULT_LIMIT_VALUE = 10


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


@require_GET
def question(request, q_id):
    question_obj = get_object_or_404(Question, id=q_id)
    if not question_obj.active:
        raise Http404()
    answers = Answer.objects.filter(question=question_obj)
    context = {
        'question': question_obj,
        'answers': answers
    }
    return render(request, 'qa/question.html', context)


def test(request, *args, **kwargs):
    return HttpResponse('OK')
