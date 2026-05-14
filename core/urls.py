from django.urls import path
from django.views.generic import RedirectView

from core.views import index
from core.views import top

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('top/', top, name='top'),
    path('top.html', RedirectView.as_view(url='/top/', permanent=True), name='top_redirect'),
]