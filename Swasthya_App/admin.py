from django.contrib import admin
from .models import Ambulance, FirstAid, Doctor, Patient
# Register your models here.

admin.site.register(Ambulance)
admin.site.register(FirstAid)
admin.site.register(Doctor)
admin.site.register(Patient)