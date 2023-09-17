from django.shortcuts import render
from .models import PriceUslugi, Uslugi, VoprosOtvet
# Create your views here.
from crm.forms import USLForm, ContactForm


def uslugi(request):    
    usl=PriceUslugi.objects.all()
    return render(request, 'nedvizhimost/uslugi.html', context={'usl':usl})




def DetailUslug(request, slug_uslug):
    uslugi = Uslugi.objects.get(slug=slug_uslug)
    form2 = ContactForm(request.POST)
    usluga_id = Uslugi.objects.get(slug=slug_uslug)
    vopotv = VoprosOtvet.objects.filter(usluga_id=usluga_id)
    usl_best = Uslugi.objects.filter( best=True)
    return render(
        request,
        'uslugi/detail_uslugi.html',
        context={'uslugi': uslugi, 'form2':form2, 'vopotv':vopotv, 'usl_best':usl_best}
    )

def usl_list(request, tipusl, h1):
    form = USLForm(request.POST)
    form2 = ContactForm(request.POST)
    usl_ofrdoc=Uslugi.objects.filter(tipusl=tipusl, tipcdelki='doc')
    usl_dogovor = Uslugi.objects.filter(tipusl=tipusl, tipcdelki='dogovor')
    usl_soprsdel = Uslugi.objects.filter(tipusl=tipusl, tipcdelki='soprsdel')
    usl_oformldoc = Uslugi.objects.filter(tipusl=tipusl, tipcdelki='oformldoc')
    usl_best=Uslugi.objects.filter(tipusl=tipusl, best=True)
    return render(request, 'nedvizhimost/uslugi_detail.html', context={'usl_ofrdoc':usl_ofrdoc, 'usl_dogovor':usl_dogovor, 'usl_soprsdel':usl_soprsdel, 'usl_oformldoc': usl_oformldoc, 'usl_best':usl_best, 'h1': h1, 'form':form})
    
    
def usl_list2(request, tipusl, h1):
    form = USLForm(request.POST)
    form2 = ContactForm(request.POST)
    zhi1=Uslugi.objects.filter(tipusl=tipusl, tipcdelki='zhi1')
    zhi2 = Uslugi.objects.filter(tipusl=tipusl, tipcdelki='zhi2')
    zhi3 = Uslugi.objects.filter(tipusl=tipusl, tipcdelki='zhi3')
    zhi4 = Uslugi.objects.filter(tipusl=tipusl, tipcdelki='zhi4')
    usl_best=Uslugi.objects.filter(tipusl=tipusl, best=True)
    return render(request, 'nedvizhimost/uslugi_detail2.html', context={'zhi1':zhi1, 'zhi2':zhi2, 'zhi3':zhi3, 'zhi4': zhi4, 'usl_best':usl_best, 'h1': h1, 'form':form})