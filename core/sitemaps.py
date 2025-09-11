from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Photo

class PhotoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Photo.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('photo_page', args=[obj.id])
