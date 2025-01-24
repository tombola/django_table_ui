import factories
from factory.django import DjangoModelFactory

from seeds.models import Crop, CropVariety


class CropFactory(DjangoModelFactory):
    class Meta:
        model = Crop

    name = factories.Faker("word")
    binomial_1 = factories.Faker("word")
    binomial_2 = factories.Faker("word")
    created_at = factories.Faker("date_time_this_year")
    updated_at = factories.Faker("date_time_this_year")



class CropVarietyFactory(DjangoModelFactory):
    class Meta:
        model = CropVariety

    name = factories.Faker("word")
    crop = factories.SubFactory(CropFactory)
    created_at = factories.Faker("date_time_this_year")
    updated_at = factories.Faker("date_time_this_year")