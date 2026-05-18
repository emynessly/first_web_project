from django.urls import path
from django.views.generic import RedirectView

from core.views import index, top, catalog, book_detail, contact

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('top/', top, name='top'),
    path('top.html', RedirectView.as_view(url='/top/', permanent=True), name='top_redirect'),
    path('catalog/', catalog, name='catalog'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('contact/', contact, name='contact'),
]