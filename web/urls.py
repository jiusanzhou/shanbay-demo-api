from django.conf.urls import url
from web.views import WebView

urlpatterns = [
    url(r'^', WebView.as_view()),
]