from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from catalog.models import Category
from django.core.mail import send_mail
from django.views.generic import View, TemplateView

from .forms import ContactForm


class IndexView(TemplateView):
    template_name = 'pages/index.html'
    
index = IndexView.as_view()

def contact(request):
    sucess = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail
        sucess = True
    else:
        form = ContactForm()
    context = {
        'form': form,
        'sucess': sucess
    }
    return render(request, 'pages/contact.html', context)