from django.db import models
from django.utils.text import slugify
from .my_validators import life_years_validator
from django.core.validators import RegexValidator


class LinksModel(models.Model):
    name = models.CharField(default='YouTube', max_length=12)
    link = models.URLField(default='.')
    icon = models.ImageField(upload_to='icons', default='image')

    def __str__(self):
        return self.name


class BioVelesModel(models.Model):
    bio_veles = models.TextField(default='Veles Bio', max_length=1500)
    foto_veles = models.ImageField(upload_to='veles', default='.')

    def __str__(self):
        return 'Duo Veles'


class MediaModel(models.Model):
    foto = models.ImageField(upload_to='veles', default='.')


class VelesComponentsModel(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(default='guitar', max_length=50)
    bio = models.TextField(max_length='2000')
    picture = models.ImageField(upload_to='veles_components', default='')
    slug = models.SlugField(blank=False, null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ComposerModel(models.Model):
    name = models.CharField(default='', max_length=80, )
    years = models.CharField(max_length=11, validators=[life_years_validator], blank=True, null=True)

    def __str__(self):
        return self.name


class OperaModel(models.Model):
    title = models.CharField(default='', max_length=500)
    opus = models.CharField(max_length=7, validators=[RegexValidator(r'[Oo]p\.\s?\d{1,3}')], blank=True)
    composer = models.ForeignKey(ComposerModel, on_delete=models.SET_NULL, related_name='operas', null=True)

    def __str__(self):
        return self.title


class CyclePartModel(models.Model):
    part = models.CharField(max_length=200, default='', blank=True)
    opera = models.ForeignKey(OperaModel, on_delete=models.SET_NULL, related_name='parts', null=True)

    def __str__(self):
        return self.part


class SongModel(models.Model):
    song = models.CharField(max_length=200, blank=False)
    cycle_part = models.ForeignKey(
        CyclePartModel, on_delete=models.SET_NULL, related_name='songs', null=True, blank=True
    )
    opera = models.ForeignKey(
        OperaModel, on_delete=models.SET_NULL, related_name='op_songs', null=True, blank=True
    )

    def __str__(self):
        return self.song


class VideosModel(models.Model):
    src = models.URLField(null=False, default='')
    title = models.CharField(null=False, default='', max_length=500)