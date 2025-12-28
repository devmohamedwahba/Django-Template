from django.contrib import admin

from .models.admin import AdminUser


@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "user__email",
        "is_active",
        "user__is_staff",
        "user__date_joined",
    )
    search_fields = ("username", "user__email")
    list_filter = ("user__is_active", "user__is_staff")
    ordering = ("-user__date_joined",)
