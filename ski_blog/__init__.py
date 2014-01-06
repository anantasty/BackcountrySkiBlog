from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from skiblog.models import SkiBlogPage

admin.site.register(SkiBlogPage, PageAdmin)
