from django.contrib import admin
from .models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'e_mail', 'message']
    list_editable = list_display[1:]
    ordering = ['id']


