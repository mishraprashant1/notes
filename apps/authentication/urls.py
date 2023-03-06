from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginFormView.as_view(), name='index'),
    path('signup/', SignUpFormView.as_view(), name='signup')
]
