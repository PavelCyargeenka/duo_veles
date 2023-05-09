from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from duo_veles.utils import LinksAndTitleMixin


class ContactsView(LinksAndTitleMixin, FormView):
    form_class = ContactForm
    success_url = '/success/'
    template_name = 'contact/contacts.html'

    def form_valid(self, form):
        form.save()
        try:
            send_mail(
                recipient_list=['pavelcyargeenka@gmail.com'],
                fail_silently=True,
                subject='New message from Duo Veles website contact form',
                message=
                f"""
                Name: {form.cleaned_data['name']}\n\n
                E-mail: {form.cleaned_data['e_mail']}\n\n
                Message: {form.cleaned_data['message']}\n
                """,
                from_email='infodjango47@gmail.com'
            )
            send_mail(
                recipient_list=[form.cleaned_data['e_mail']],
                fail_silently=True,
                subject='|DUO VELES| This is an automatically generated e-mail, please do not reply',
                message='Your message has been sent, thank you!',
                from_email='infodjango47@gmail.com'
            )
        except BadHeaderError:
            return HttpResponse('Bad header')
        return super(ContactsView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Contacts'
        return context


class SuccessView(LinksAndTitleMixin, TemplateView):
    template_name = 'contact/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['message'] = 'Your message has been sent successfully!'
        return context


