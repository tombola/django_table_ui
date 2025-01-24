"""
Defines a Django management command to import crop varieties from a CSV file.

The command reads the CSV file, validates each row against the CropVarietySchema, and creates
CropVariety objects in the database for valid rows. If there are validation errors, they are
printed to the console.

Usage:
    import_crop_varieties <file_path>

Args:
    file_path (str): The path to the CSV file containing crop variety data.

Raises:
    ValueError: If there are validation errors in the CSV data.

Example:
    import_crop_varieties('/path/to/crop_varieties.csv').

"""

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
@click.argument("file_path", type=click.Path(exists=True))
def import_crop_varieties(file_path:str) -> None:  # noqa: D103
    with Path(file_path).open("r") as file:
        csv_content = file.read()
        csv_file = StringIO(csv_content)
        csv_reader = csv.DictReader(csv_file)

        validated_data: list[CropVarietySchema] = []
        errors = []

        for row in csv_reader:
            try:
                validated_data.append(CropVarietySchema(**row))
            except ValueError as e:
                errors.append(f"Row {csv_reader.line_num}: {str(e)}")

        if errors:
            click.echo(click.style("Validation errors:", fg='red'))
            for error in errors:
                click.echo(click.style(error, fg='red'))

            if not click.confirm("There were validation errors. Do you want to continue importing valid rows?"):
                return

        for data in validated_data:
            click.echo(data.dict())
            CropVariety.objects.create(**data.dict())

        click.echo(click.style(f"Successfully imported {len(validated_data)} rows", fg="green"))
