from django.urls import path
from .views import *

urlpatterns = [
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('success/', SuccessView.as_view(), name='success'),
]

