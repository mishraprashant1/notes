from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginFormView.as_view(), name='auth_index'),
    path('signup/', SignUpFormView.as_view(), name='signup'),
    path('sign-out/', SignOut.as_view(), name='sign_out')
]
