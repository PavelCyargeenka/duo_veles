from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import *
from duo_veles.utils import LinksAndTitleMixin


class IndexView(LinksAndTitleMixin, TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Duo Veles'
        context['allow'] = \
            'accelerometer; autoplay; clipboard-write; encrypted-media; ' \
            'gyroscope; picture-in-picture; web-share'
        context['videos'] = VideosModel.objects.all()
        return context


class BioView(LinksAndTitleMixin, TemplateView):
    template_name = 'main/bio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(
            {
                'bio': BioVelesModel.objects.get(id=1),
                'title': 'bio',
                'pavel': VelesComponentsModel.objects.get(name__icontains='Pavel'),
                'mateja': VelesComponentsModel.objects.get(name__icontains='Mateja')
            }
        )
        return context


class BioVelesComponentView(LinksAndTitleMixin, DetailView):
    model = VelesComponentsModel
    template_name = 'main/bio_veles_component.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        component = VelesComponentsModel.objects.get(slug=self.kwargs['slug'])
        context['component'] = component
        return context


class MediaView(LinksAndTitleMixin, ListView):
    template_name = 'main/media.html'
    model = MediaModel
    ordering = ['id']
    context_object_name = 'pictures'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Gallery'
        return context


class RepertoireView(LinksAndTitleMixin, ListView):
    template_name = 'main/repertoire.html'
    model = ComposerModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Repertoire'
        context['composers'] = ComposerModel.objects.all()

        return context
