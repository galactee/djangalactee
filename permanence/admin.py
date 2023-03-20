from django.contrib import admin

from permanence.models import PermanenceDay


@admin.register(PermanenceDay)
class PermanenceDayAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Date", {"fields": ("date",)}),
        ("Position 1", {"fields": ("inscrite_1", "call_amount_1", "call_duration_1")}),
        ("Position 2", {"fields": ("inscrite_2", "call_amount_2", "call_duration_2")}),
        ("Position 3", {"fields": ("inscrite_3", "call_amount_3", "call_duration_3")}),
        ("Position 4", {"fields": ("inscrite_4", "call_amount_4", "call_duration_4")}),
    )

    list_display = ("date", "inscrite_1", "inscrite_2", "inscrite_3", "inscrite_4")
