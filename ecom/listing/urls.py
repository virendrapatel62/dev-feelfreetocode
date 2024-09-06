
from django.urls import path
from .views import product_listing_view, product_details_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('shop/', product_listing_view),
    path('product/<int:id>/', product_details_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
