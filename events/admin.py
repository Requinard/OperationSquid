from django.contrib import admin

from models import *
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "registration_open", "event_date")
    list_filter = ("registration_open", "event_date")

    search_fields = ("name", "location", "description")

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("id", "related_event", "related_user", "paid")
    list_filter = ("paid", "date_paid")

    list_search = ("related_user__username", "related_event__name")

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "related_registration")
    list_filter = ("related_registration__related_event",)

class AccessAdmin(admin.ModelAdmin):
    list_display = ("id", "related_registration")
    list_filter = ("related_registration__related_event",)

admin.site.register(Event, EventAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Access, AccessAdmin)
admin.site.register(Payment, PaymentAdmin)