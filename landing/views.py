from django.core.mail import send_mail
from django.shortcuts import render
from landing.models import Toys
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import Http404
from django.views.decorators.cache import cache_page

from landing.forms import OrderForm


def index(request):
    toys = Toys.objects.all()
    return (render_to_response('index.html',
                               {
                                   'toys': toys,
                                   'form': OrderForm()
                               }, context_instance=RequestContext(request))
    )


def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        form.is_valid()
        page = form.save()
        subject = "Заказ игрушки"
        sender = 'webmaster@mimimi-toys.ru'
        recipients = ['order@mimimi-toys.ru']
        toy = Toys.objects.get(id=form.cleaned_data['toy_id'])
        t = loader.get_template('email.txt')
        c = Context({
            'form': form.cleaned_data,
            'toy' : toy
        })
        send_mail(subject, t.render(c), sender, recipients)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')




