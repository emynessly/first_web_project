from django.urls import path
from django.views.generic import RedirectView

from core.views import index, top, catalog, book_detail, contact, book_create, book_edit, register, add_comment

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('top/', top, name='top'),
    path('top.html', RedirectView.as_view(url='/top/', permanent=True), name='top_redirect'),
    path('catalog/', catalog, name='catalog'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('contact/', contact, name='contact'),
    path('book/create/', book_create, name='book_create'),
    path('book/<int:pk>/edit/', book_edit, name='book_edit'),
    path('accounts/register/', register, name='register'),
    path('book/<int:pk>/comment/', add_comment, name='add_comment'),
]