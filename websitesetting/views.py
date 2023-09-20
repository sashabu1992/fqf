from django.shortcuts import render
from .models import  VoprosOtvet, Revius_klient
# Create your views here.
from django.db.models import Q
from .forms import VoprosOtvetForm


def vopros_otvet(request):
    dataset=VoprosOtvet.objects.all()
    form = VoprosOtvetForm(request.GET)
    count = ""
    if request.GET:
        querry=request.GET.get('vopros')
        dataset=VoprosOtvet.objects.filter(Q(vopros__icontains=querry))
        count = VoprosOtvet.objects.filter(Q(vopros__icontains=querry)).count()
    
    return render(request, 'nedvizhimost/vopros_otvet.html',  context={'dataset':dataset, 'form':form, 'count': count})


def reviews(request):
    revius_klient = Revius_klient.objects.all()
    return render(request, 'nedvizhimost/reviews.html', context={'revius_klient': revius_klient,})
