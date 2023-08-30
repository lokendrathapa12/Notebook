from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    phone = models.BigIntegerField()
    permanentaddress = models.CharField(max_length=100)
    residencialaddress = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)


class CourcesModel(models.Model):
    COURCES_NAME = (
        ('BSCCSIT','BSCCSIT'),
        ('BSC','BSC'),
        ('BIT','BIT'),
        ('BCA','BCA'),
        ('B.TECH','B.TECH'),
        ('BBS','BBS'),
        ('BBA','BBA'),
        ('B.ED','B.ED'),
        ('+2 SCIENCE','+2 SCIENCE'),
        ('+2 MANAGEMENT','+2 MANAGEMENT'),
        ('+2 EDUCATION','+2 EDUCATION'),
    )
    YEAR_CHOICES = (
        ('First Year', 'First Year'),
        ('Second Year', 'Second Year'),
        ('Third Year', 'Third Year'),
        ('Fourth Year', 'Fourth Year'),
    )
    SEMESTER_CHOICES = (
        ('First Semester','First Semester'),
        ('Second Semester','Second Semester'),
        ('Third Semester','Third Semester'),
        ('Fourth Semester','Fourth Semester'),
        ('Fifth Semester','Fifth Semester'),
        ('Six Semester','Six Semester'),
        ('Seven Semester','Seven Semester'),
        ('Eight Semester','Eight Semester'),
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null= True)
    cname = models.CharField(max_length=100,choices=COURCES_NAME)
    shortdetail = models.CharField(max_length=300) 
    year = models.CharField(max_length=100,choices=YEAR_CHOICES)
    semester = models.CharField(max_length=100,choices=SEMESTER_CHOICES)
    subject = models.CharField(max_length=160)
    oldquestion = models.FileField(upload_to='notebook/media')
    oldquestionyear = models.DateField(auto_now_add=False)
    syllabus = models.FileField(upload_to='notebook/file')
    syllabuspublishdate = models.DateTimeField(auto_now_add=False)
    note = models.FileField(upload_to='notebook/note')
    notepublishdate = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=100)
