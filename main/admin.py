from django.contrib import admin
from .models import Facility, Department

from .models import Facility, Department, Employee, Coaching, Certification, CorrectiveAction

admin.site.register(Facility)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Coaching)
admin.site.register(Certification)
admin.site.register(CorrectiveAction)