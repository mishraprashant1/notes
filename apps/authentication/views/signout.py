from django.views.generic.base import RedirectView
from django.contrib.auth import logout


class SignOut(RedirectView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return '/auth'
