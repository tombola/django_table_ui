from django.db import models


class Crop(models.Model):
    """
    Model representing a crop with its binomial name.

    Attributes:
        name (str): The common name of the crop.
        binomial_1 (str): The first part of the binomial name.
        binomial_2 (str): The second part of the binomial name.
        created_at (datetime): The timestamp when the crop was created.
        updated_at (datetime): The timestamp when the crop was last updated.

    Methods:
        __str__(): Returns the string representation of the crop.
        binomial_name (property): Returns the full binomial name if both parts
        are present, otherwise None.

    """

    name = models.CharField(max_length=100, blank=False)
    binomial_1 = models.CharField(max_length=100)
    binomial_2 = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.binomial_1} {self.binomial_2})"

    @property
    def binomial_name(self) -> str | None:
        if self.binomial_1 and self.binomial_2:
            return f"{self.binomial_1} {self.binomial_2}"
        return None


class CropVariety(models.Model):
    """
    Represents a variety of a crop, ie a seed product.

    Attributes:
        crop (ForeignKey): Reference to the associated Crop model.
        name (CharField): Name of the crop variety.
        description (TextField): Description of the crop variety.
        created_at (DateTimeField): Timestamp when the crop variety was created.
        updated_at (DateTimeField): Timestamp when the crop variety was last
        updated.

    """

    crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        if self.crop and self.crop.binomial_name:
            f"{self.name} ({self.crop.binomial_1} {self.crop.binomial_2})"

        return self.name
