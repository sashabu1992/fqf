from django.shortcuts import render
from .models import  VoprosOtvet
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

