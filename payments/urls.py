from django.urls import path

from .views import get_item_view


urlpatterns = [
    path("item/<int:id>/", get_item_view, name="items"),
]
