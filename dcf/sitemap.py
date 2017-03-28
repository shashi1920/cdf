from django.contrib.sitemaps import Sitemap
from django.conf import settings

from dcf.models import Item


class ItemSitemap(Sitemap):
    def changefreq(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return obj.updated

    def items(self):
        return Item.objects.all()[:settings.DCF_SITEMAP_LIMIT]

sitemaps_dict = {
    'Item': ItemSitemap,
    }
