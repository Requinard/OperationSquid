from django.contrib import admin
import models
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "related_user", "related_event")
    list_filter = ("related_event","related_categories")

    search_fields = ("related_user__username", "related_event__name", "title", "body")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Message, MessageAdmin)