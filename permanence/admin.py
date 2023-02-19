from django.contrib import admin

from permanence.models import PermanenceDay


@admin.register(PermanenceDay)
class PermanenceDayAdmin(admin.ModelAdmin):
    pass
