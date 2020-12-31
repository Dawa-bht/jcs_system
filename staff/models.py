from django.db import models
from students.validators import *

# Staff Detail


class StaffDetail(models.Model):
    Employee_ID = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=30, blank=True)
    date_of_birth = models.DateField(
        auto_now=False, auto_now_add=False, blank=True)
    CID = models.CharField(max_length=11, unique=True,
                           blank=True, validators=[validate_cid])

    Administration = 'Administration'
    TeachingStaff = 'Teaching Staff'
    NonTeachingStaff = 'Non Teaching Staff'
    SupportingStaff = 'Supporting Staff'
    Category_choices = [(Administration, 'Administration'),
                        (TeachingStaff, 'Teaching Staff'),
                        (NonTeachingStaff, 'Non Teaching Staff'),
                        (SupportingStaff, 'Supporting Staff'), ]
    category = models.CharField(
        choices=Category_choices, max_length=30, blank=True)

    position_title = models.CharField(max_length=50, blank=True)
    position_level = models.CharField(max_length=10, blank=True)
    grade = models.CharField(max_length=5, blank=True)
    appointment_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True)
    joining_date_of_present_school = models.DateField(
        auto_now=False, auto_now_add=False, blank=True)
    transfered_from = models.CharField(max_length=50, blank=True)

    Regular = 'Regular'
    Contract = 'Contract'
    Employment_choices = [(Regular, 'Regular'), (Contract, 'Contract')]
    Employment_type = models.CharField(
        choices=Employment_choices, max_length=30, blank=True)

    nationality = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    qualification = models.TextField(blank=True)
    contact_number = models.CharField(
        max_length=8, blank=True, validators=[validate_phone])
    email = models.EmailField(blank=True, validators=[validate_email])
    permanent_address = models.TextField(blank=True)
    profile_pic = models.ImageField(
        upload_to="images/staff", default='/static/images/user.jpg', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.name, self.position_title)
