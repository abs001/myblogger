from django.contrib import admin
from .models import SiteConfiguration, Blog

admin.site.register(SiteConfiguration)
admin.site.register(Blog)
