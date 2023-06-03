from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label=_('Email'))
    first_name = forms.CharField(label=_('First name'))
    last_name = forms.CharField(label=_('Last name'))

    class Meta:
        model = User
        fields = [_('username'),
                  _('first_name'),
                  _('last_name'),
                  _('email'),
                  _('password1'),
                  _('password2'),
                  ]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save()
        commons = Group.objects.get(name="commons")
        user.groups.add(commons)
        return user


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="common users")
        user.groups.add(common_users)

        send_mail(
            subject=('Welcome to our News Portal!'),
            message=f'{user.username}, you have successfully registered!',
            from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
            recipient_list=[user.email],)

        return user
