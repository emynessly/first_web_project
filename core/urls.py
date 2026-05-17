from django.urls import path
from django.views.generic import RedirectView

from core.views import index
from core.views import top
from core.views import catalog

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('top/', top, name='top'),
    path('top.html', RedirectView.as_view(url='/top/', permanent=True), name='top_redirect'),
    path('catalog/', catalog, name='catalog'),
]