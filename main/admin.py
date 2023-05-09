from django.contrib import admin
from .models import *


@admin.register(BioVelesModel)
class BioVelesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'bio_veles', 'foto_veles']
    list_editable = list_display[1:]


@admin.register(VelesComponentsModel)
class VelesComponentsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'instrument', 'bio', 'picture', 'slug']
    list_editable = list_display[1:]
    ordering = ['name']


@admin.register(MediaModel)
class MediaModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'foto']
    list_editable = list_display[1:]


@admin.register(LinksModel)
class LinksModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'icon']
    list_editable = list_display[1:]


@admin.register(ComposerModel)
class ComposerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'years']
    list_editable = list_display[1:]
    ordering = ['id']


@admin.register(OperaModel)
class OperaModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'opus', 'composer']
    list_editable = list_display[1:]
    ordering = ['id']


@admin.register(CyclePartModel)
class CyclePartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'part', 'opera']
    list_editable = list_display[1:]
    ordering = ['id']


@admin.register(SongModel)
class SongModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'song', 'cycle_part', 'opera']
    list_editable = list_display[1:]
    ordering = ['id']


@admin.register(VideosModel)
class VideosModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'src', 'title']
    list_editable = list_display[1:]
    ordering = ['id']
