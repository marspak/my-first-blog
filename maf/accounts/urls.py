from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .forms import LoginForm
from . import views as accounts_views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'authentication_form': LoginForm}, name='login_url'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/accounts/login/',}, name='logout_url'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^signup_ok/$', TemplateView.as_view(template_name='registration/signup_ok.html'), name='signup_ok'),
]