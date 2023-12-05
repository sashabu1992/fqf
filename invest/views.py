from django.shortcuts import render
from crm.forms import  ContactForm
from .models import Invest, GalleryDom, TagInvest
# Create your views here.
def InvestPost(request):
    invest = Invest.objects.filter(is_draft=True)
    gallery = GalleryDom.objects.filter()
    tag = TagInvest.objects.filter()

    form2 = ContactForm(request.POST)
    return render(
        request,
        'invest/invest_list.html',
        context={'form2':form2, 'invest':invest, 'gallery':gallery, 'tag':tag }
    )


def InvestDeteil(request):

    form2 = ContactForm(request.POST)
    return render(
        request,
        'invest/invest_detail.html',
        context={'form2':form2, }
    )
