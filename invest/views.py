from django.shortcuts import render
from crm.forms import  ContactForm
from .models import Invest, GalleryDom, TagInvest
from .forms import InvestFilterForms

# Create your views here.
def InvestPost(request):
    invest = Invest.objects.filter(is_draft=True)
    form = InvestFilterForms(request.GET)

    gallery = GalleryDom.objects.filter()
    tag = TagInvest.objects.filter()
    form2 = ContactForm(request.POST)

    if form.is_valid():
        print("------------------111111111-------------------")
        if form.cleaned_data["min_price"]:
            invest = invest.filter(price__gte=form.cleaned_data["min_price"])
        if form.cleaned_data["max_price"]:
            invest = invest.filter(price__lte=form.cleaned_data["max_price"])
        if form.cleaned_data["min_pl"]:
            invest = invest.filter(ploshad__gte=form.cleaned_data["min_pl"])
        if form.cleaned_data["max_pl"]:
            invest = invest.filter(ploshad__lte=form.cleaned_data["max_pl"])
        if form.cleaned_data["tipcdelki"]:
            invest = invest.filter(tipcdelki__in=form.cleaned_data["tipcdelki"])
        if form.cleaned_data["deistvie"]:
            invest = invest.filter(deistvie__in=form.cleaned_data["deistvie"])
        if form.cleaned_data["colkomnat"]:
            invest = invest.filter(colkomnat__in=form.cleaned_data["colkomnat"])
    return render(
        request,
        'invest/invest_list.html',
        context={'form2':form2, 'invest':invest, 'gallery':gallery, 'tag':tag, 'form':form,  }
    )


def InvestDeteil(request, slug_invest):
    investpost = Invest.objects.get(is_draft=True, slug=slug_invest)
    gallery = GalleryDom.objects.filter(invest_id=1)
    form2 = ContactForm(request.POST)
    return render(
        request,
        'invest/invest_detail.html',
        context={'form2':form2, 'investpost':investpost, 'gallery':gallery }
    )
