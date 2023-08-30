from django.contrib import admin
from .models import CourcesModel,Profile
# Register your models here.
@admin.register(CourcesModel)
class CourceAdminModel(admin.ModelAdmin):
    list_display = ['cname','year','semester','subject','oldquestion','oldquestionyear','syllabus','syllabuspublishdate','shortdetail','note','notepublishdate','writer']


@admin.register(Profile)
class ProfileAdminModel(admin.ModelAdmin):
    list_display = ['user','phone','permanentaddress','residencialaddress','qualification']