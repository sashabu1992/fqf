from multiprocessing.reduction import register

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Dom, GalleryDom, Gorod, Ulica, Rajon, Komplex
from django.views.generic import TemplateView, ListView, DetailView
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.http import HttpResponseRedirect
from .forms import DomFilterForms
from django.http import JsonResponse, HttpResponse, JsonResponse

from crm.forms import NedvForm


@csrf_exempt
def nedvizhimost_list(request, template, category, h1):
    if category == '':
        filter = Dom.objects.filter(is_draft=True)
    else:
        filter = Dom.objects.filter(is_draft=True, category=category)
    form = DomFilterForms(request.GET)
    otvet = request.GET
    vibor_tipcdelki = otvet.getlist('tipcdelki')
    vibor_category = otvet.getlist('category')
    vibor_colkomnat = otvet.getlist('colkomnat')
    if otvet.get('gorod'):
        vibor_gorod = Gorod.objects.filter(id=int(otvet.get('gorod')))
    else:
        vibor_gorod = ''
    if otvet.get('rajon'):
        vibor_rajon = Rajon.objects.filter(id=int(otvet.get('rajon')))
    else:
        vibor_rajon = ''
    if otvet.get('ulica'):
        vibor_ulica = Ulica.objects.filter(id=int(otvet.get('ulica')))
    else:
        vibor_ulica = ''
    if otvet.get('komplex'):
        vibor_komplex = Komplex.objects.filter(id=int(otvet.get('komplex')))
    else:
        vibor_komplex = ''

    vibor_min_price = otvet.get('min_price')
    vibor_max_price = otvet.get('max_price')
    vibor_min_pl = otvet.get('min_pl')
    vibor_max_pl = otvet.get('max_pl')

    if form.is_valid():
        print("------------------111111111-------------------")
        if form.cleaned_data["min_price"]:
            filter = filter.filter(price__gte=form.cleaned_data["min_price"])
        if form.cleaned_data["max_price"]:
            filter = filter.filter(price__lte=form.cleaned_data["max_price"])
        if form.cleaned_data["min_pl"]:
            filter = filter.filter(ploshad__gte=form.cleaned_data["min_pl"])
        if form.cleaned_data["max_pl"]:
            filter = filter.filter(ploshad__lte=form.cleaned_data["max_pl"])
        if form.cleaned_data["tipcdelki"]:
            filter = filter.filter(tipcdelki__in=form.cleaned_data["tipcdelki"])
        if form.cleaned_data["category"]:
            filter = filter.filter(category__in=form.cleaned_data["category"])
        if form.cleaned_data["gorod"]:
            filter = filter.filter(gorod__exact=form.cleaned_data["gorod"])
        if form.cleaned_data["rajon"]:
            filter = filter.filter(rajon__exact=form.cleaned_data["rajon"])
        if form.cleaned_data["ulica"]:
            filter = filter.filter(ulica__exact=form.cleaned_data["ulica"])
        if form.cleaned_data["komplex"]:
            filter = filter.filter(komplex__exact=form.cleaned_data["komplex"])
        if form.cleaned_data["colkomnat"]:
            filter = filter.filter(colkomnat__in=form.cleaned_data["colkomnat"])

    return render(
        request,
        template,
        context={'filter': filter, 'form': form, 'otvet': otvet,
                 'vibor_gorod': vibor_gorod,
                 'vibor_ulica': vibor_ulica,
                 'vibor_rajon': vibor_rajon,
                 'vibor_tipcdelki': vibor_tipcdelki,
                 'vibor_tipcdelki': vibor_tipcdelki,
                 'vibor_komplex': vibor_komplex,
                 'vibor_category': vibor_category,
                 'vibor_min_price': vibor_min_price,
                 'vibor_max_price': vibor_max_price,
                 'vibor_min_pl': vibor_min_pl,
                 'vibor_max_pl': vibor_max_pl,
                 'vibor_colkomnat': vibor_colkomnat,
                 'h1': h1}

    )



def DetailPosts(request, slug_dom):
    form = NedvForm(request.POST)
    dom = Dom.objects.get(slug=slug_dom)
    gallery = GalleryDom.objects.filter(dom=dom)
    #строчку ниже надо проверять так как может не работать
    post = Dom.objects.get(slug=slug_dom, is_draft=True)
    fav = bool
    if post.favorit.filter(id=request.user.id).exists():
        fav = True 
    return render(
        request,
        'nedvizhimost/detail_nedvizhimost.html',
        context={'dom': dom, 'gallery': gallery, 'form': form, 'fav': fav }
    )
    
    
def ajaxbest(request, id):
    res = {'error': False}
    dom = get_object_or_404(Dom, id=id)
    if dom.favorit.filter(id=request.user.id).exists():
        dom.favorit.remove(request.user)
    else:
        dom.favorit.add(request.user)
    return JsonResponse(res)


def best_list(request, template, h1):
    filter = Dom.objects.filter(is_draft=True, best=True)

    # post = get_object_or_404(Dom, slug=slug_dom, is_draft=True, best=True)
    fav = bool
    # if post.favorit.filter(id=request.user.id).exists():
    #    fav = True
    return render(
        request,
        template,
        context={'filter': filter, 'h1': h1, 'fav': fav}

    )


