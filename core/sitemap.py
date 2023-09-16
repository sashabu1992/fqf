from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from nedvizhimost.models import Dom

class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return ['glav', 'about', 'contatcs', 'partner', 'spetcs', 'politika', 'nedvizhimost_list','maps_list','komerch_list','kvartir_list','garazhi_list','newstroi_list','best_list','yurusl','rieltusl','vopros_otvet']
    

    def location(self, item):
        return reverse(item)
        
class DynamicViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1

    def items(self):
        return Dom.objects.all()

    def location(self, item):
        # return reverse('news-page', args=[item.pk])
        return f'/catalog/{item.slug}/'