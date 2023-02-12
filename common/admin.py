from django.contrib import admin

from common.models import Benevole


class BenevoleAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "statut",
        "is_staff",
        "is_active",
    )

    list_filter = ("is_active", "statut")


admin.site.register(Benevole, BenevoleAdmin)
