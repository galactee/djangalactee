from datetime import date

from django.db import models
from django.db.models import Q

from common.models import Benevole


class PermanenceDayManager(models.Manager):
    def for_given_month(self, year, month):
        return self.filter(date__year=year, date__month=month).order_by("date")

    def for_benevole(self, benevole: Benevole):
        return self.filter(
            Q(inscrite_1=benevole)
            | Q(inscrite_2=benevole)
            | Q(inscrite_3=benevole)
            | Q(inscrite_4=benevole)
        )

    def future(self):
        return self.filter(date__gte=date.today())


class PermanenceDay(models.Model):
    objects = PermanenceDayManager()
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date.strftime("%A %d %B %Y")

    @property
    def inscrites(self):
        return list(filter(None, (self.inscrite_at_position(i) for i in range(1, 5))))

    def inscrite_at_position(self, position):
        if position == 1:
            return self.inscrite_1
        if position == 2:
            return self.inscrite_2
        if position == 3:
            return self.inscrite_3
        if position == 4:
            return self.inscrite_4

    inscrite_1 = models.ForeignKey(
        Benevole, on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )
    inscrite_2 = models.ForeignKey(
        Benevole, on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )
    inscrite_3 = models.ForeignKey(
        Benevole, on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )
    inscrite_4 = models.ForeignKey(
        Benevole, on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )

    call_amount_1 = models.PositiveSmallIntegerField(
        "Nombre d'appels 1", blank=True, null=True
    )
    call_amount_2 = models.PositiveSmallIntegerField(
        "Nombre d'appels 2", blank=True, null=True
    )
    call_amount_3 = models.PositiveSmallIntegerField(
        "Nombre d'appels 3", blank=True, null=True
    )
    call_amount_4 = models.PositiveSmallIntegerField(
        "Nombre d'appels 4", blank=True, null=True
    )

    call_duration_1 = models.PositiveSmallIntegerField(
        "Durée d'appel 1", blank=True, null=True
    )
    call_duration_2 = models.PositiveSmallIntegerField(
        "Durée d'appel 2", blank=True, null=True
    )
    call_duration_3 = models.PositiveSmallIntegerField(
        "Durée d'appel 3", blank=True, null=True
    )
    call_duration_4 = models.PositiveSmallIntegerField(
        "Durée d'appel 4", blank=True, null=True
    )

    class Meta:
        verbose_name = "Jour de Permanence"
        verbose_name_plural = "Jours de Permanence"
