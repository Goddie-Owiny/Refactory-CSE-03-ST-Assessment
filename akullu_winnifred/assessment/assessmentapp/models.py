from django.db import models
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import re
from django.db import models
from django.core.validators import MinLengthValidator



#letter validation
def validate_letters(value):
    if not re.match("^([a-zA-Z]+\s)*[a-zA-Z]+$", value):
        raise ValidationError("Only letters are allowed.")

#number validation function
def validate_numbers(value):
    if not re.match("^[0-9]*$", value):
        raise ValidationError("Only numbers are allowed.")

#contact length validation function
def validate_contact_length(value):
    if len(value) != 10:
        raise ValidationError("Contact field must contain exactly 10 digits.")



# Create your models here.

class Reg(models.Model):

    COURSE_CHOICES = (
        ('Certificate in Health Science','Certificate in Health Science'),
        ('Certificate in Apllied Technology','Certificate in Applied Technology'),
        ('Bachelor of information technology','Bachelor of Information Technology'),
        ('Bachelors in Business Technology','Certificate in Health Science'),
        ('Master of Public Health','Master of Public Health'),
    )
    ENTRY_SCHEME = (
    ('A-Level certificate','A-Level certificate'),
    ('Adult/Mature Learning','Adult/Mature Learning'),
    ('Certificate','Certificate'),
    ('Diploma','Diploma'),
    ('Bachelors','Bachelors'),
    )
    INTAKE_CHOICES = (
    ('January Intake','January Intake'),
    ('May Intake','May Intake'),
    ('August Intake','August Intake'),
    )
    SPONSORSHIP_CHOICES = (
    ('Private','Private'),
    ('Government','Government'),
    ('Bursary','Bursary'),
    )
    GENDER_CHOICES = (
    ('Male','Male'),
    ('Female','Female'),
    )

    fname = models.CharField(max_length=50,validators=[validate_letters,MinLengthValidator(3)])
    lname = models.CharField(max_length=50,validators=[validate_letters,MinLengthValidator(3)])
    course = models.CharField(max_length=200,choices=COURSE_CHOICES)
    entryscheme = models.CharField(max_length=200,choices=ENTRY_SCHEME)
    intake = models.CharField(max_length=200,choices=INTAKE_CHOICES)
    sponsorship = models.CharField(max_length=200,choices=SPONSORSHIP_CHOICES)
    gender = models.CharField(max_length=200,choices=GENDER_CHOICES)
    dob = models.DateField(default=timezone.now)
    residence = models.CharField(max_length=255,validators=[validate_letters,MinLengthValidator(2)])

    def __str__(self):
        return f"{self.fname} {self.lname}"

