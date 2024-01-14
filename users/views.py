from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth import login, authenticate
from django_email_verification import send_email
from django.contrib.auth.models import Group
from django.views.generic import UpdateView
from .models import *
from django.db import transaction
from django.urls import reverse_lazy
from .forms import ProfileUpdateForm, UserUpdateForm
from nedvizhimost.models import Dom
from invest.models import Invest, GalleryDom

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user_group = Group.objects.get(name='users')
			user.groups.add(user_group)
			username = form.cleaned_data.get('username')
			messages.success(request, f'Создан аккаунт {username}! Подтвердите регистрацию ссылкой на почте')
			# высылаем письмо и делаем его неактивным
			user.is_active = False
			send_email(user)
			return redirect('register')
	else:
		form = UserRegisterForm()
	return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
	return render(request, 'registration/profile.html')

class ProfileEditView(UpdateView):
    """
    Представление для редактирования профиля пользователя.
    """
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'registration/profile-edit.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование профиля пользователя: {self.request.user.username}'
        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super(ProfileEditView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile')


@ login_required
def favourite_list(request):
    new = Dom.objects.filter(favorit=request.user)
    new2 = Invest.objects.filter(favorite_invest=request.user)
    gallery = GalleryDom.objects.filter()
    return render(request,
                  'registration/favourites.html',
                  {'new': new, 'new2':new2, 'gallery':gallery})


@ login_required
def favourite_add(request, id):
    dom = get_object_or_404(Dom, id=id)
    if dom.favorit.filter(id=request.user.id).exists():
        dom.favorit.remove(request.user)
    else:
        dom.favorit.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@ login_required
def favourite_add2(request, id):
    invest = get_object_or_404(Invest, id=id)
    if invest.favorit.filter(id=request.user.id).exists():
        invest.favorit.remove(request.user)
    else:
        invest.favorit.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])