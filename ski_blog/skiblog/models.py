from django.db import models
from mezzanine.pages.models import Page
from taggit.managers import TaggableManager

class SkiBlogPage(Page):
    SNOW_TYPES = (
        ('P', 'Powder'),
        ('I', 'Icy'),
        ('PP', 'Packed Powder')
    )
    COVER_TYPE = (
        ('L', 'Low'),
        ('M', 'Moderate'),
        ('G', 'Good')
    )
    date = models.DateTimeField('Date of the tour', null=True, blank=True)
    snow_type = models.CharField(max_length=5, choices=SNOW_TYPES)
    snow_cover = models.CharField(max_length=5, choices=COVER_TYPE)
    snow_depth = models.IntegerField('Snow Depth in cm')
    tour_name = models.CharField('Name of Tour', null=True, blank=True, max_length=200)
    tour_area = models.CharField('Tour Area', null=True, blank=True, max_length=200)
    tour_trailhead = models.CharField('Tour Trailhead', null=True, blank=True, max_length=200)
    tour_region = models.CharField('Region', null=True, blank=True, max_length=200)
    tour_city = models.CharField('City', null=True, blank=True, max_length=200)
    tour_state = models.CharField('State', null=True, blank=True, max_length=200)
    tour_country = models.CharField('Country', null=True, blank=True, max_length=200)
    partners = TaggableManager()


class TourImages(models.Model):
    skiblogpage = models.ForeignKey(SkiBlogPage)
    image = models.ImageField(upload_to='images')


class SkiUser(models.Model):
    user = models.OneToOneField("auth.User")
    bio = models.TextField()
