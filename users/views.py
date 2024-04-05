import random
import string

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, FormView

from users.forms import UserRegisterForm, UserProfileForm, RestoreUserForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        new_user.save()
        send_mail(
            subject='Поздравляем с регистрацией!',
            message='Вы зарегистрированы на нашей платформе',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        return self.request.user


def generate_random_password():
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


class RestoreUser(FormView):
    template_name = 'users/new_password.html'
    form_class = RestoreUserForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = User.objects.filter(email=email).first()
        new_password = generate_random_password()
        user.password = make_password(new_password)
        user.save()
        send_mail(
            subject='Смена пароля',
            message=f'У Вашего аккаунта новый пароль: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False
        )
        return super().form_valid(form)

