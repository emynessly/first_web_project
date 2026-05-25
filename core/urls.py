from django.urls import path
from django.views.generic import RedirectView

from core.views import index, top, CatalogListView, BookDetailView, contact, BookCreateView, BookUpdateView, register, add_comment, BookDeleteView

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('top/', top, name='top'),
    path('top.html', RedirectView.as_view(url='/top/', permanent=True), name='top_redirect'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('contact/', contact, name='contact'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('accounts/register/', register, name='register'),
    path('book/<int:pk>/comment/', add_comment, name='add_comment'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]