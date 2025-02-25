from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Item


def get_item_view(request: HttpRequest, id: int) -> HttpResponse:
    item = get_object_or_404(Item, id=id)
    template = "items.html"
    return render(request, template, {"item": item})
