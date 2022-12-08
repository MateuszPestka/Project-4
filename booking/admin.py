from django.contrib import admin
from .models import Booking

admin.site.register(Booking)


class BookingAdmin(admin.ModelAdmin):

    list_display = ('date', 'time', 'first_name', 'last_name', 'approved', 'vip')
    search_fields = ['date', 'time', 'first_name', 'last_name']
    list_filter = ('approved', 'vip')
    actions = ['approve_booking', 'make_vip']

    def approve_booking(self, request, queryset):
        queryset.update(approved=True)

    def make_vip(self, request, queryset):
        queryset.update(vip=True)
