from django import forms
from profiles.models import LandingHypothesisRegistration

class LHRForm(forms.ModelForm):
    class Meta:
        model = LandingHypothesisRegistration
