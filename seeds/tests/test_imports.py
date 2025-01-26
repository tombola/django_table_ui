import os
from pathlib import Path

import pytest
from django.core import management
from django.core.management.base import CommandError

from seeds.models import CropVariety


@pytest.fixture
def import_csv_path() -> str:
    """Return the path to the CSV file to import."""
    return os.getenv("TEST_IMPORT_ACQ_CSV_PATH", "/path/to/crop_varieties.csv")


@pytest.fixture
def import_all_csv_path() -> str:
    """Return the path to the CSV file to import."""
    return os.getenv("TEST_IMPORT_ALL_ACQ_CSV_PATH", "/path/to/crop_varieties.csv")


@pytest.mark.django_db
def test_import_crop_varieties(import_csv_path) -> None:
    """
    Test the 'import_crop_varieties' management command.

    This test attempts to run the 'import_crop_varieties' command with a specified CSV file path.
    If the command raises a CommandError, the test will fail with an appropriate
    message.

    Args:
        import_csv_path (str): The path to the CSV file to be imported.

    Raises:
        pytest.fail: If the management command 'import_crop_varieties' fails.

    """
    management.call_command(
        "import_crop_varieties",
        import_csv_path,
        force=True,
    )
    assert CropVariety.objects.count() == 1
    assert CropVariety.objects.first().name == "Spring onion - White Lisbon"
    assert str(CropVariety.objects.first()) == "Spring onion - White Lisbon"


@pytest.mark.django_db
def test_import_all_crop_varieties(import_all_csv_path) -> None:
    management.call_command(
        "import_crop_varieties",
        import_all_csv_path,
        force=True,
    )
    assert CropVariety.objects.count() == 341
    assert CropVariety.objects.get(sku="OnWl")
