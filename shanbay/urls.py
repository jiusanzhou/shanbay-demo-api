from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^.*', include('web.urls')),
]

#urlpatterns = format_suffix_patterns(urlpatterns)