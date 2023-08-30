from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('signin/',views.registartion, name='registrationpage'),
    path('accounts/login/',views.loginview, name='loginpage'),
    path('logout/',views.logout_view, name='logoutpage'),
    path('profile/',views.profile, name='profilepage'),
    path('bsccsit/',views.bsccsit, name='bsccsitpage'),
    path('bsc/',views.bsc, name='bscpage'),
    path('bba/',views.bba, name='bbapage'),
    path('bbs/',views.bbs, name='bbspage'),
    path('bca/',views.bca, name='bcapage'),
    path('bed/',views.bed, name='bedpage'),
    path('bit/',views.bit, name='bitpage'),
    path('btech/',views.btech, name='btechpage'),
    path('education/',views.education, name='educationpage'),
    path('management/',views.management, name='managementpage'),
    path('science/',views.science, name='sciencepage'),
    path('noteform/',views.NoteUploadFormView,name='noteform'),
]+static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
