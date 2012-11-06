from django.contrib import admin

from profiles.models import LandingHypothesisRegistration


class LandingHypothesisRegistrationAdmin(admin.ModelAdmin):
    pass

admin.site.register(LandingHypothesisRegistration, LandingHypothesisRegistrationAdmin)
