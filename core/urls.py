from django.conf.urls import url
from core.views import HomeTemplateView

urlpatterns = [
    url(r'^$', HomeTemplateView.as_view()),
]