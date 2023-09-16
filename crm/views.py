from django.views.generic import CreateView
from .models import Feedback
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm

