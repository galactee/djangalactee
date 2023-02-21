from factory.django import DjangoModelFactory
from factory.faker import Faker

from common.models import Benevole


class BenevoleFactory(DjangoModelFactory):
    class Meta:
        model = Benevole

    is_active = True
    is_staff = False
    email = Faker("email")
    username = Faker("slug")
