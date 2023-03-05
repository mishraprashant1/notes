from .forms import *
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
import uuid


class SignUpFormView(FormView):
    template_name = 'authentication/signup.html'
    form_class = SignUpForm
    success_url = '/notes/'

    def form_valid(self, form):

        data = form.cleaned_data

        username = uuid.uuid4().hex[:30]
        email = data['email']
        password = data['password']

        user = User.objects.create_user(username=username, email=email, password=password)

        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.save()

        return super().form_valid(form)
