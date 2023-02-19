from factory.django import DjangoModelFactory

from permanence.models import PermanenceDay


class PermanenceDayFactory(DjangoModelFactory):
    class Meta:
        model = PermanenceDay
