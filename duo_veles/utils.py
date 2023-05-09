from main.models import LinksModel

navbar_dict = {
    'index': 'Home',
    'bio_veles': 'Bio',
    'media': 'Gallery',
    'repertoire': 'Repertoire',
    'contacts': 'Contacts',
}


class LinksAndTitleMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = LinksModel.objects.all()
        context['navbar_dict'] = navbar_dict
        return context
