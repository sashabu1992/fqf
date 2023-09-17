from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views import generic
from nedvizhimost.models import Dom
from uslugi.models import Uslugi
from websitesetting.models import  Baher, Partner, BankPartner, Revius_klient, OficeImg, PlusVam
from nedvizhimost.forms import DomFilterForms


from django.views.generic import CreateView
from crm.models import Feedback
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from crm.forms import ContactForm, NedvForm, PartnerForm, USLForm





def about(request):    
    form = ContactForm(request.POST)
    return render(request, 'nedvizhimost/about.html', context={'form':form,})



# Функция отправки сообщения
def email(subject, content):
   send_mail(subject,
      content,
      'info@fqf-nedvizhimost.ru',
      ['sashabu1992@gmail.com', 'mr.alekseyromanov@yandex.ru', 'fqf-nedvizhimost@yandex.ru']
   )

# Функция, которая вернет сообщение в случае успешного заполнения формы
def success(request):
    res = {'error': False}
    form = ContactForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            # Формируем сообщение для отправки
            data = form.data
            subject = f'Форма БЕСПЛАТНАЯ КОНСУЛЬТАЦИЯ '
            telo = f'Сообщение от {data["user"]} Телефон: {data["phone"]} '
            email(subject, telo)
            form.save()

    return JsonResponse(res)

# Функция, которая вернет сообщение в случае успешного заполнения формы
def success2(request):
    res = {'error': False}
    form = NedvForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            # Формируем сообщение для отправки
            data = form.data
            subject = f'Форма БЕСПЛАТНАЯ КОНСУЛЬТАЦИЯ '
            telo = f'Сообщение от {data["user"]} Телефон: {data["phone"]} Сообщение: {data["content"]} '
            email(subject, telo)
            form.save()
    return JsonResponse(res)

# Функция, которая вернет сообщение в случае успешного заполнения формы
def success3(request):
    res = {'error': False}
    form = PartnerForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            # Формируем сообщение для отправки
            data = form.data
            print(data)
            subject = f'Форма СТАТЬ ПАРТНЕРОМ '
            telo = f'Сообщение от {data["user"]} Телефон: {data["phone"]} Компания: {data["content"]} '
            email(subject, telo)
            form.save()
    return JsonResponse(res)

def glav(request):
    best = Dom.objects.filter(best=True)
    baher = Baher.objects.all()
    revius_klient = Revius_klient.objects.all()
    plus = PlusVam.objects.all()
    partner = Partner.objects.all()
    oficeimg = OficeImg.objects.all()
    form = DomFilterForms(request.GET)
    bankpartner = BankPartner.objects.all()
    filter = Dom.objects.filter(is_draft=True)
    form2 = ContactForm(request.POST)
    return render(
        request,
        'nedvizhimost/index.html',
        context={'filter':filter, 'form':form, 'baher': baher, 'plus':plus, 'partner':partner, 'revius_klient':revius_klient,'oficeimg':oficeimg, 'bankpartner':bankpartner, 'best':best, 'form2':form2}
        )


def contatcs(request):    
    return render(request, 'nedvizhimost/contacts.html')

def politika(request):    
    return render(request, 'nedvizhimost/politic.html')


def spetcs(request):    
    return render(request, 'nedvizhimost/spetcs.html')

def partner(request):    
    bankpartner = BankPartner.objects.all()
    partner = Partner.objects.all()
    form = ContactForm(request.POST)
    form2 = PartnerForm(request.POST)
    form3= USLForm(request.POST)
    usl=Uslugi.objects.all()
    return render(request, 'nedvizhimost/partner.html',
        context={'bankpartner':bankpartner, 'partner':partner, 'form': form, 'form2': form2, 'form3': form3, 'usl':usl}
        )

def page_not_found_view(request, exception):
    return render(request, 'nedvizhimost/404.html', status=404)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    