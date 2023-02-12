from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Benevole(AbstractUser):
    class Statut(models.TextChoices):
        ANIMATRICE = "AN", "Animatrice"
        EN_FORMATION = "AF", "Active en formation"
        ANCIENNE = "AL", "Ancienne"  # al for alumni
        SYMPATHISANTE = "SY", "Sympathisante"

    statut = models.CharField(
        "Statut", max_length=2, choices=Statut.choices, default=Statut.EN_FORMATION
    )

    is_staff = models.BooleanField("Admin site")
    is_active = models.BooleanField("Compte activé")

    class Meta:
        verbose_name = "Bénévole"
        verbose_name_plural = "Bénévoles"
