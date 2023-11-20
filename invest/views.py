from django.shortcuts import render
from crm.forms import  ContactForm
# Create your views here.
def InvestPost(request):

    form2 = ContactForm(request.POST)
    return render(
        request,
        'invest/invest_list.html',
        context={'form2':form2, }
    )


def InvestDeteil(request):

    form2 = ContactForm(request.POST)
    return render(
        request,
        'invest/invest_detail.html',
        context={'form2':form2, }
    )
