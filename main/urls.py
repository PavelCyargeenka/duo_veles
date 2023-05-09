from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('bio/', BioView.as_view(), name='bio_veles'),
    path('bio/<slug:slug>/', BioVelesComponentView.as_view(), name='bio_component'),
    path('media/', MediaView.as_view(), name='media'),
    path('repertoire/', RepertoireView.as_view(), name='repertoire'),
]

