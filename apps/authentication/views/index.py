from .forms import *
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class LoginFormView(FormView):
    template_name = 'authentication/login.html'
    form_class = LoginForm
    success_url = '/notes/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Log In'
        context['title'] = 'Log In'
        context['login_active'] = True
        return context

    def form_valid(self, form):

        data = form.cleaned_data

        email = data['email']
        username = User.objects.get(email=email)
        password = data['password']
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            print('--->Login Successful!')
        else:
            print('--->Invalid Login')

        return super().form_valid(form)
