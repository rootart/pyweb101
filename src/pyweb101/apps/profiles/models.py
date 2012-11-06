from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class LandingHypothesisRegistration(models.Model):
    email = models.EmailField(_("Email"), unique=True)
    first_name = models.CharField(_("First name"), max_length=255)
    last_name = models.CharField(_("Last name"), max_length=255)
    date_of_birth = models.DateField(_("Date of birth"), blank=True, null=True)
    is_student = models.BooleanField(_("Are you a student?"))
    university = models.CharField(_("University"), max_length=255,
        blank=True, null=True
    )
    faculty = models.CharField(_("Faculty"), max_length=255,
        blank=True, null=True
    )
    major = models.CharField(_("What is your major?"), max_length=255,
        blank=True, null=True
    )
    uuid = models.CharField(_("Unique identifier of request"), max_length=255,
        unique=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Landing page hypothesis registration")
        verbose_name_plural = _("Landing page hypothesis registrations")
        ordering = ('created', )

    def __unicode__(self):
        return self.email
