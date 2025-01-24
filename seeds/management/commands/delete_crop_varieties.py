import csv
from io import StringIO
from pathlib import Path

import djclick as click
from django.core.management import call_command
from django.core.management.base import BaseCommand
from ninja import Schema

from seeds.api.schemas import CropSchema, CropVarietySchema
from seeds.models import CropVariety


@click.command()
def delete_crop_varieties():
    if not click.confirm('Are you sure you want to delete all crop varieties?'):
        click.echo('Operation cancelled.')
        return

    CropVariety.objects.all().delete()
    click.echo('All crop varieties have been deleted.')