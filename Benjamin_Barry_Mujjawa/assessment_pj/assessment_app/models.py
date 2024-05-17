from django.db import models

# Create your models here.
class Student(models.Model):
    # course = [
    #     ('ICT', 'ICT'),
    #     ('Medicine', 'Medicine'),
    #     ('Education', 'Education'),
    # ]

    # entry_scheme = [
    #     ('A-Level certificate', 'A-Level certificate'),
    #     ('Adult/Mature Learning', 'Adult/Mature Learning'),
    #     ('Certificate', 'Certificate'),
    #     ('Diploma', 'Diploma'),
    #     ('Bachelors', 'Bachelors'),
    # ]

    # intake = [
    #     ('January Intake', 'January Intake'),
    #     ('May Intake', 'May Intake'),
    #     ('August Intake', 'August Intake'),
    # ]

    # sponsorships = [
    #     ('Private', 'Private'),
    #     ('Government', ' Government'),
    #     ('Bursary', 'Bursary'),
    # ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.CharField(max_length=100)#, choices={'course': 'course'})
    entry_scheme = models.CharField(max_length=50) # , choices={'entry_scheme': 'entry_scheme'})
    intake = models.CharField(max_length=50) #, choices={'intake': 'intake'})
    sponsorship = models.CharField(max_length=50) #, choices={'sponsorship': 'sponsorship'})
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    residence = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
