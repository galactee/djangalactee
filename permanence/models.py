from django.db import models

from common.models import Benevole


class PermanenceDayManager(models.Manager):
    pass


class PermanenceDay(models.Model):
    objects = PermanenceDayManager
    date = models.DateField(unique=True)

    inscrite_1 = models.ForeignKey(
        Benevole, on_delete=models.SET_NULL, null=True, related_name="+"
    )
    inscrite_2 = models.ForeignKey(
        Benevole, on_delete=models.SET_NULL, null=True, related_name="+"
    )
    inscrite_3 = models.ForeignKey(
        Benevole, on_delete=models.SET_NULL, null=True, related_name="+"
    )
    inscrite_4 = models.ForeignKey(
        Benevole, on_delete=models.SET_NULL, null=True, related_name="+"
    )

    call_amount_1 = models.PositiveSmallIntegerField(null=True)
    call_amount_2 = models.PositiveSmallIntegerField(null=True)
    call_amount_3 = models.PositiveSmallIntegerField(null=True)
    call_amount_4 = models.PositiveSmallIntegerField(null=True)

    call_duration_1 = models.PositiveSmallIntegerField(null=True)
    call_duration_2 = models.PositiveSmallIntegerField(null=True)
    call_duration_3 = models.PositiveSmallIntegerField(null=True)
    call_duration_4 = models.PositiveSmallIntegerField(null=True)
