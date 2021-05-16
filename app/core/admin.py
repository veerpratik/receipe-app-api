from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "name"]
    # this is used when we have to
    #  update user through admin panel.
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    # this used when we have add user from admin panel
    add_fieldsets = (
        (None, {"classes": ("wide",),
         "fields": ("email", "password1", "password2")}),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)
