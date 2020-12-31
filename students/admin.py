from django.contrib import admin
from .models import std_registration_form, DisciplinaryIssue, CharacterCertificate

admin.site.register(std_registration_form)
admin.site.register(DisciplinaryIssue)
admin.site.register(CharacterCertificate)
