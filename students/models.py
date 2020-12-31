from django.db import models
from .validators import *
from staff.models import StaffDetail

# Student details


class std_registration_form(models.Model):
    student_code = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)

    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=30)

    seven = '7'
    eight = '8'
    nine = '9'
    ten = '10'
    eleven = '11'
    twelve = '12'
    class_choices = [(seven, '7'), (eight, '8'), (nine, '9'),
                     (ten, '10'), (eleven, '11'), (twelve, '12')]
    standard = models.CharField(choices=class_choices, max_length=30)

    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    section_choices = [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E')]
    section = models.CharField(choices=section_choices, max_length=30)

    General = 'General'
    Agriculture = 'Agriculture'
    Environmental_Science = 'Environmental Science'
    Economics = 'Economics'
    Media = 'Media'
    Commerce = 'Commerce'
    Arts = 'Arts'
    Science = 'Science'

    stream_choices = [
        (General, 'General'),
        (Agriculture, 'Agriculture'),
        (Environmental_Science, 'Environmental Science'),
        (Economics, 'Economics'),
        (Media, 'Media'),
        (Commerce, 'Commerce'),
        (Arts, 'Arts'),
        (Science, 'Science')
    ]
    Stream = models.CharField(choices=stream_choices,
                              max_length=30, blank=True)

    date_of_birth = models.DateField(
        auto_now=False, auto_now_add=False, blank=True)
    admission_no = models.BigIntegerField(blank=True)
    date_of_admission = models.DateField(
        blank=True, auto_now=False, auto_now_add=False)
    email = models.EmailField(blank=True)
    CID = models.CharField(max_length=11, unique=True, blank=True)
    class_teacher = models.ForeignKey(
        StaffDetail, null=True, on_delete=models.CASCADE)
    previous_school = models.CharField(max_length=50, blank=True)
    mobile_number = models.CharField(max_length=8, blank=True)
    permanent_address = models.TextField(blank=True)
    Boarder = 'Boarder'
    Dayscholar = 'Dayscholar'
    BoarderOrDayscholar = [(Boarder, 'Boarder'), (Dayscholar, 'Dayscholar')]
    BoarderOrDayscholar = models.CharField(
        choices=BoarderOrDayscholar, blank=True, max_length=30)
    Regular = 'Regular'
    Repeater = 'Repeater'
    RegularOrRepeater = [(Regular, 'Regular'), (Repeater, 'Repeater')]
    RegularOrRepeater = models.CharField(
        choices=RegularOrRepeater, blank=True, max_length=30)
    profile_pic = models.ImageField(
        upload_to="images/students", default='/static/images/user.jpg', null=True, blank=True)
    father_name = models.CharField(max_length=50, blank=True)
    mother_name = models.CharField(max_length=50, blank=True)
    fathers_occupation = models.CharField(max_length=50, blank=True)
    mothers_occupation = models.CharField(max_length=50, blank=True)
    parents_mobile_number = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.name, self.standard, self.section)


class DisciplinaryIssue(models.Model):
    Student = models.ForeignKey(
        std_registration_form, null=True, on_delete=models.CASCADE)
    Violation_detail = models.TextField()
    Violation_date = models.DateField(auto_now=False, auto_now_add=False)
    Warning_decision = models.TextField()
    Approved_by = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.Student)


class CharacterCertificate(models.Model):
    Student = models.ForeignKey(
        std_registration_form, null=True, on_delete=models.CASCADE)

    Special_Recognization = 'Special_Recognition'
    Volunteerism = 'Volunteerism'
    Academic = 'Academic'
    Games_Sports = 'Games and Sports'
    Literary = 'Literary'
    Cultural = 'Cultural'
    Category_choices = [
        (Special_Recognization, 'Special_Recognition'),
        (Volunteerism, 'Volunteerism'),
        (Academic, 'Academic'),
        (Games_Sports, 'Games and Sports'),
        (Literary, 'Literary'),
        (Cultural, 'Cultural')
    ]
    Category = models.CharField(choices=Category_choices, max_length=30)
    Description = models.TextField()
    Awarded_on = models.DateField(auto_now=False, auto_now_add=False)
    Awarded_by = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.Student)
