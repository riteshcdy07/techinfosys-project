from django.contrib import admin
from .models import Service,Technology
from .models import ContactMessage

# Register your models here.
admin.site.register(Service)
admin.site.register(Technology)





@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "service",
        "created_at",
    )

    search_fields = ("name", "email", "phone", "message")
    list_filter = ("service", "created_at")
    readonly_fields = ("created_at",)