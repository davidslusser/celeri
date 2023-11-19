from django.contrib import admin

# import models
from casemgr.models import (Booking,
                            Court,
                            CourtType,
                            Case,
                            CaseFile,
                            Defendant,
                            Defender,
                            Hearing,
                            HearingType,
                            Judge,
                            Prosecutor
                            )


class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'booking_id']
    search_fields = ['id', 'booking_id']
    list_filter = []


class CourtAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'name', 'address', 'city', 'state', 'zip_code', 'court_type']
    search_fields = ['id', 'name', 'address', 'city', 'state', 'zip_code']
    list_filter = ['court_type']


class CourtTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'name', 'description', 'enabled']
    search_fields = ['id', 'name', 'description']
    list_filter = ['enabled']


class CaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'case_number', 'title', 'booking', 'defendant']
    search_fields = ['id', 'case_number', 'title']
    list_filter = ['booking', 'defendant']


class CaseFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'title', 'url']
    search_fields = ['id', 'title', 'url']
    list_filter = []


class DefendantAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'title', 'first_name', 'last_name', 'dob', 'sex', 'address', 'city', 'state', 'zip_code']
    search_fields = ['id', 'title', 'first_name', 'last_name', 'dob', 'sex', 'address', 'city', 'state', 'zip_code']
    list_filter = []


class DefenderAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'title', 'first_name', 'last_name', 'address', 'city', 'state', 'zip_code']
    search_fields = ['id', 'title', 'first_name', 'last_name', 'address', 'city', 'state', 'zip_code']
    list_filter = []


class HearingAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'case', 'hearing_date', 'judge', 'hearing_type']
    search_fields = ['id', 'hearing_date']
    list_filter = ['case', 'judge', 'hearing_type']


class HearingTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'enabled']
    search_fields = ['id', 'name', 'description']
    list_filter = ['enabled']


class JudgeAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'title', 'first_name', 'last_name']
    search_fields = ['id', 'title', 'first_name', 'last_name']
    list_filter = []


class ProsecutorAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'title', 'first_name', 'last_name', 'address', 'city', 'state', 'zip_code']
    search_fields = ['id', 'title', 'first_name', 'last_name', 'address', 'city', 'state', 'zip_code']
    list_filter = []


# register models
admin.site.register(Booking, BookingAdmin)
admin.site.register(Court, CourtAdmin)
admin.site.register(CourtType, CourtTypeAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(CaseFile, CaseFileAdmin)
admin.site.register(Defendant, DefendantAdmin)
admin.site.register(Defender, DefenderAdmin)
admin.site.register(Hearing, HearingAdmin)
admin.site.register(HearingType, HearingTypeAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(Prosecutor, ProsecutorAdmin)
