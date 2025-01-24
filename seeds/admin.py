"""
Admin configuration for the Crop model.

This module registers the Crop model with the Django admin site and customizes
the admin interface for the Crop model.

Classes:
    CropAdmin: Custom admin interface for the Crop model.
"""

from django.contrib import admin

from seeds.models import Crop, CropVariety


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):  # noqa: D101
    list_display = ("name", "binomial_1", "binomial_2")
    search_fields = ("name", "binomial_1", "binomial_2")


@admin.register(CropVariety)
class CropVarietyAdmin(admin.ModelAdmin):  # noqa: D101
    list_display = ("name", "crop", "created_at", "updated_at")
    search_fields = ("name", "crop__name")
