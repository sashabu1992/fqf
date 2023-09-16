from django import forms
from .models import *





class DomFilterForms(forms.Form):
    min_price = forms.IntegerField(label="от",  required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'от', 'min': 0 }))
    max_price = forms.IntegerField(label="до", required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'до', 'min': 0 }))
    min_pl = forms.IntegerField(label="от", required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'от', 'min': 0 }))
    max_pl = forms.IntegerField(label="до", required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'до', 'min': 0 }))
    tipcdelki = forms.MultipleChoiceField(choices=TIPCDELKI_CHOISE, required=False, widget=forms.CheckboxSelectMultiple())
    category = forms.MultipleChoiceField(choices=CATEGORY_CHOISE, required=False,  widget=forms.CheckboxSelectMultiple())
    gorod = forms.ModelChoiceField(queryset=Gorod.objects.all(), required=False)
    colkomnat = forms.MultipleChoiceField(choices=COL_KOMNAT, required=False)
    rajon = forms.ModelChoiceField(queryset=Rajon.objects.all(), required=False)
    ulica = forms.ModelChoiceField(queryset=Ulica.objects.all(), required=False)
    komplex = forms.ModelChoiceField(queryset=Komplex.objects.all(), required=False)