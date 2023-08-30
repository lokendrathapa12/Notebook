from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import login,logout,authenticate
from .forms import RegistrationForm,LoginForm,NoteUploadForm
from .models import CourcesModel,Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    return render(request, 'notebook/home.html')
#SIGNIN PAGE
def registartion(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = RegistrationForm()
    return render(request, 'notebook/signin.html',{'form':fm})    

#LOGIN PAGE
def loginview(request):
    if request.method  == 'POST':
        fm = LoginForm(request=request, data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username = uname, password = upass)
            login(request, user)
            return HttpResponseRedirect('/profile/')
    else:
        fm = LoginForm()
    return render(request, 'notebook/login.html',{'form':fm})

def logout_view(request):
    logout(request)
    return render(request, 'notebook/home.html')

#PROFILE PAGE
@login_required
def profile(request):
    user = Profile.objects.all()
    return render(request, 'notebook/profile.html',{'user':user})

#CSIT PAGE
@login_required
def bsccsit(request):
    itnote = CourcesModel.objects.filter(cname='BSCCSIT')
    return render(request,'notebook/bsccsit.html',{'itnote':itnote})

#BSC PAGE
@login_required
def bsc(request):
    itnote = CourcesModel.objects.filter(cname='BSC')
    return render(request,'notebook/bsc.html',{'itnote':itnote})

#BBA PAGE
@login_required
def bba(request):
    itnote = CourcesModel.objects.filter(cname='BBA')
    return render(request,'notebook/bba.html',{'itnote':itnote})

#BBS PAGE
@login_required
def bbs(request):
    itnote = CourcesModel.objects.filter(cname='BBS')
    return render(request,'notebook/bbs.html',{'itnote':itnote})

#BCA PAGE
@login_required
def bca(request):
    itnote = CourcesModel.objects.filter(cname='BCA')
    return render(request,'notebook/bca.html',{'itnote':itnote})

#BED PAGE
@login_required
def bed(request):
    itnote = CourcesModel.objects.filter(cname='B.ED')
    return render(request,'notebook/bed.html',{'itnote':itnote})

#BIT PAGE
@login_required
def bit(request):
    itnote = CourcesModel.objects.filter(cname='BIT')
    return render(request,'notebook/bit.html',{'itnote':itnote})

#BTECH PAGE
@login_required
def btech(request):
    itnote = CourcesModel.objects.filter(cname='B.TECH')
    return render(request,'notebook/btech.html',{'itnote':itnote})

#+2 EDUCATION PAGE
@login_required
def education(request):
    itnote = CourcesModel.objects.filter(cname='+2 EDUCATION')
    return render(request,'notebook/education.html',{'itnote':itnote})

#+2 MANAGEMENT PAGE
@login_required
def management(request):
    itnote = CourcesModel.objects.filter(cname='+2 MANAGEMENT')
    return render(request,'notebook/management.html',{'itnote':itnote})

#+2 SCIENCE PAGE
@login_required
def science(request):
    itnote = CourcesModel.objects.filter(cname='+2 SCIENCE')
    return render(request,'notebook/science.html',{'itnote':itnote})

@login_required
def NoteUploadFormView(request):
    if request.method== 'POST':
        fm = NoteUploadForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/profile/')
    else:
        fm = NoteUploadForm
    return render(request,'notebook/noteupload.html',{'fm':fm})