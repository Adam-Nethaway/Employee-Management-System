from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Facility(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)  # Optional address or location details

    def __str__(self):
        return self.name


class Department(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)

    supervisor = models.ForeignKey(
        "Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="supervised_departments",
        limit_choices_to={"position": 3},  # Only Supervisors can be selected
    )

    def __str__(self):
        return self.name

# Create your models here.
class Employee(models.Model):
    HOURS_FULL_TIME = 1
    HOURS_PART_TIME = 2
    HOURS_CHOICES = [
        (HOURS_FULL_TIME, "Full-Time"),
        (HOURS_PART_TIME, "Part-Time"),
    ]

    POSITION_DCA = 1
    POSITION_ICQA = 2
    POSITION_SUPERVISOR = 3
    POSITION_MANAGER = 4
    POSITION_CHOICES = [
        (POSITION_DCA, "DCA"),
        (POSITION_ICQA, "ICQA"),
        (POSITION_SUPERVISOR, "Supervisor"),
        (POSITION_MANAGER, "Process Manager"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to Django's User model
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    racfid = models.CharField(max_length=7, unique=True)
    hours = models.IntegerField(choices=[(1, "Full-Time"), (2, "Part-Time")], default=1)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    position = models.IntegerField(choices=[(1, "DCA"), (2, "ICQA"), (3, "Supervisor"), (4, "Process Manager")], default=1)
    supervisor = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="supervisees", limit_choices_to={"position": 3}
    )
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    facility = models.ForeignKey(Facility, on_delete=models.SET_NULL, null=True, blank=True)
    gear_access = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.racfid})"
    

    
class Certification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="certifications")
    name = models.CharField(max_length=100)
    date_earned = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)  # Some expire, some don’t

    def __str__(self):
        return f"{self.name} - {self.employee.first_name} {self.employee.last_name}"
    

class CorrectiveAction(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="corrective_actions")
    reason = models.CharField(max_length=255)
    issued_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="issued_corrective_actions")
    date_issued = models.DateField(auto_now_add=True)
    resolution = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Action for {self.employee.first_name} {self.employee.last_name} - {self.reason}"
       


class Coaching(models.Model):
    CATEGORY_BEHAVIOR = 1
    CATEGORY_ATTENDANCE = 2
    CATEGORY_SAFETY = 3
    CATEGORY_GRAINGER = 4

    CATEGORY_CHOICES = [
        (CATEGORY_BEHAVIOR, "Behavior"),
        (CATEGORY_ATTENDANCE, "Attendance"),
        (CATEGORY_SAFETY, "Safety"),
        (CATEGORY_GRAINGER, "Grainger Principles"),
    ]

    TYPE_RECOGNITION = 1
    TYPE_DEVELOPMENT = 2

    TYPE_CHOICES = [
        (TYPE_RECOGNITION, "Recognition"),
        (TYPE_DEVELOPMENT, "Development"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="coachings")
    category_type = models.IntegerField(choices=TYPE_CHOICES)
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.employee.first_name} {self.employee.last_name}"

