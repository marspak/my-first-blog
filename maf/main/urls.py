from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views as main_views

urlpatterns = [
    url(r'^$', main_views.home, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
]