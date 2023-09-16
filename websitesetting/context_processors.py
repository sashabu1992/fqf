from .models import WebsiteSettings, WebsiteContent
from crm.forms import Contact2Form

def website_settings(request):
    formbase = Contact2Form(request.POST)
    web_settings = WebsiteSettings.objects.filter(language='ru').first()
    web_content = WebsiteContent.objects.filter(language='ru').first()
    url_get = request.get_full_path 
    s = str(url_get)
    url_get = s[s.find("?") + 0:]
    url_get = "'".join(url_get.split("'")[:-1])
    return {'web_settings': web_settings, 'web_content': web_content, 'url_get':url_get, 'formbase': formbase,}