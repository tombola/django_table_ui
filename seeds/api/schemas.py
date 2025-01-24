from typing import Any

from ninja import Field, ModelSchema, Schema

from seeds.models import Crop, CropVariety


class CropSchema(ModelSchema):
    class Meta:
        model = Crop
        fields = ("name", "binomial_1", "binomial_2")

# class CropVarietySchema(ModelSchema):
#     class Meta:
#         model = CropVariety
#         fields = ("name", "crop")

class CropVarietySchema(Schema):
    name: str = Field(..., alias="c_Crop_Variety", min_length=1)
