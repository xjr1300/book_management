from django.contrib import admin

from .models import Division


class DivisionAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "created_at",
        "updated_at",
    )


admin.site.register(Division, DivisionAdmin)
