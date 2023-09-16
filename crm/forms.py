from django.forms import ModelForm
from django.forms import Textarea, TextInput
from .models import Feedback


class ContactForm(ModelForm):

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Feedback
        # Поля, которые будем использовать для заполнения
        fields = ['subject', 'user', 'phone']
        widgets = {
        	 'subject': TextInput(
                attrs={
                    'value': 'БЕСПЛАТНАЯ КОНСУЛЬТАЦИЯ',
                    'type': 'hidden'
                	}
            	),
        	 'user': TextInput(
                attrs={
                    'placeholder': 'Ваше имя',
                    'class': 'form-control'
                	}
            	),
        	 'phone': TextInput(
                attrs={
                    'placeholder': '+7(',
                    'class': 'form-control'
                	}
            	)
        }

class Contact2Form(ModelForm):

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Feedback
        # Поля, которые будем использовать для заполнения
        fields = ['subject', 'user', 'phone', 'content']
        widgets = {
        	 'subject': TextInput(
                attrs={
                    'value': 'ЗАПОЛНИТЕ ФОРМУ',
                    'type': 'hidden'
                	}
            	),
        	 'user': TextInput(
                attrs={
                    'placeholder': 'Ваше имя',
                    'class': 'form-control'
                	}
            	),
        	 'phone': TextInput(
                attrs={
                    'placeholder': '+7(',
                    'class': 'form-control'
                	}
            	),
            	'content': Textarea(
                attrs={
                    'placeholder': 'Ваш вопрос',
                    'class': 'form-control'
                	}
            	),
        	 
        }

class NedvForm(ModelForm):
    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Feedback
        # Поля, которые будем использовать для заполнения
        fields = ['subject', 'user', 'phone']
        widgets = {
             'subject': TextInput(
                attrs={
                    'value': 'СТРАНИЦА НЕДВИЖИМОСТИ',
                    'type': 'hidden'
                    }
                ),
             'user': TextInput(
                attrs={
                    'placeholder': 'Ваше имя',
                    'class': 'form-control'
                    }
                ),
             'phone': TextInput(
                attrs={
                    'placeholder': '+7(',
                    'class': 'form-control'
                    }
                )
        }
        
        
class PartnerForm(ModelForm):
    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Feedback
        # Поля, которые будем использовать для заполнения
        fields = ['subject', 'user', 'phone', 'content']
        widgets = {
             'subject': TextInput(
                attrs={
                    'value': 'СТАТЬ ПАРТНЕРОМ',
                    'type': 'hidden'
                    }
                ),
             'user': TextInput(
                attrs={
                    'placeholder': 'Ваше имя',
                    'class': 'form-control'
                    }
                ),
            'content': TextInput(
                attrs={
                    'placeholder': 'Название компании',
                    'class': 'form-control'
                    }
                ),
             'phone': TextInput(
                attrs={
                    'placeholder': '+7(',
                    'class': 'form-control'
                    }
                )
        }

class USLForm(ModelForm):
    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Feedback
        # Поля, которые будем использовать для заполнения
        fields = ['subject', 'user', 'phone']
        widgets = {
             'subject': TextInput(
                attrs={
                    'value': 'СТРАНИЦА УСЛУГИ',
                    'type': 'hidden'
                    }
                ),
             'user': TextInput(
                attrs={
                    'placeholder': 'Ваше имя',
                    'class': 'form-control'
                    }
                ),
             'phone': TextInput(
                attrs={
                    'placeholder': '+7(',
                    'class': 'form-control'
                    }
                )
        }