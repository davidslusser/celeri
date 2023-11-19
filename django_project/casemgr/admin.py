from django.contrib import admin

# import models
from casemgr.models import (Booking,
                            Court,
                            Case,
                            CaseFile,
                            Defendant,
                            Defender,
                            Hearing,
                            Judge,
                            Prosecutor
                            )


class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'address', 'city', 'state', 'zip_code', 'email_address', 'phone_number', 'title', 'first_name', 'middle_name', 'last_name', 'dob', 'sex', 'booking_id', 'booking_officer', 'arresting_officer', 'details']
    search_fields = ['id', 'address', 'city', 'state', 'zip_code', 'email_address', 'phone_number', 'title', 'first_name', 'middle_name', 'last_name', 'dob', 'sex', 'booking_id', 'booking_officer', 'arresting_officer', 'details']
    list_filter = ['sex']


class CourtAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'name', 'address', 'city', 'state', 'zip_code', 'court_type']
    search_fields = ['id', 'name', 'address', 'city', 'state', 'zip_code', 'court_type']
    list_filter = ['court_type']


class CaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'case_number', 'title', 'booking', 'defendant']
    search_fields = ['id', 'case_number', 'title']
    list_filter = ['booking', 'defendant']


class CaseFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'title', 'url']
    search_fields = ['id', 'title', 'url']
    list_filter = []


class DefendantAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'address', 'city', 'state', 'zip_code', 'email_address', 'phone_number', 'title', 'first_name', 'middle_name', 'last_name', 'dob', 'sex']
    search_fields = ['id', 'address', 'city', 'state', 'zip_code', 'email_address', 'phone_number', 'title', 'first_name', 'middle_name', 'last_name', 'dob', 'sex']
    list_filter = ['sex']


class DefenderAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'address', 'city', 'state', 'zip_code', 'email_address', 'phone_number', 'title', 'first_name', 'middle_name', 'last_name']
    search_fields = ['id', 'address', 'city', 'state', 'zip_code', 'email_address', 'phone_number', 'title', 'first_name', 'middle_name', 'last_name']
    list_filter = []


class HearingAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'case', 'hearing_date', 'judge', 'hearing_type']
    search_fields = ['id', 'hearing_date', 'hearing_type']
    list_filter = ['case', 'judge', 'hearing_type']


class JudgeAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'address', 'city', 'state', 'zip_code', 'email_address', 'phone_number', 'title', 'first_name', 'middle_name', 'last_name']
    search_fields = ['id', 'address', 'city', 'state', 'zip_code', 'email_address', 'phone_number', 'title', 'first_name', 'middle_name', 'last_name']
    list_filter = []


class ProsecutorAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'address', 'city', 'state', 'zip_code', 'email_address', 'phone_number', 'title', 'first_name', 'middle_name', 'last_name']
    search_fields = ['id', 'address', 'city', 'state', 'zip_code', 'email_address', 'phone_number', 'title', 'first_name', 'middle_name', 'last_name']
    list_filter = []


# register models
admin.site.register(Booking, BookingAdmin)
admin.site.register(Court, CourtAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(CaseFile, CaseFileAdmin)
admin.site.register(Defendant, DefendantAdmin)
admin.site.register(Defender, DefenderAdmin)
admin.site.register(Hearing, HearingAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(Prosecutor, ProsecutorAdmin)
