from django.http import HttpResponse
from django.shortcuts import render

from .models import CropVariety


def varieties_view(request) -> HttpResponse:  # noqa: ANN001, D103
    varieties = CropVariety.objects.select_related("crop").all()
    return render(request, "seeds/varieties_list.html", {"varieties": varieties})
