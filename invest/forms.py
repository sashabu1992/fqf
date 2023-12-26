from django import forms
from .models import *

class InvestFilterForms(forms.Form):
    min_price = forms.IntegerField(label="от",  required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'от', 'min': 0 }))
    max_price = forms.IntegerField(label="до", required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'до', 'min': 0 }))
    min_pl = forms.IntegerField(label="от", required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'от', 'min': 0 }))
    max_pl = forms.IntegerField(label="до", required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'до', 'min': 0 }))
    deistvie = forms.MultipleChoiceField(choices=DEISTVIE_CHOISE, required=False )
    tipcdelki = forms.MultipleChoiceField(choices=TIP_CHOISE, required=False)
    colkomnat = forms.MultipleChoiceField(choices=COL_KOMNAT, required=False)
    country = forms.MultipleChoiceField(choices=COUNTRY, required=False)
    gotov = forms.MultipleChoiceField(choices=GOTOV, required=False)
    drugoe = forms.MultipleChoiceField(choices=DRUGOE, required=False)
