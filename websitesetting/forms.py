from django.forms import ModelForm
from django.forms import Textarea, TextInput
from .models import VoprosOtvet


class VoprosOtvetForm(ModelForm):

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = VoprosOtvet
        # Поля, которые будем использовать для заполнения
        fields = ['vopros']
        widgets = {
             'vopros': TextInput(
                attrs={
                    'placeholder': 'Поиск по разделу',
                    'type': 'text',
                    'name': 'q'
                    }
                )
        }