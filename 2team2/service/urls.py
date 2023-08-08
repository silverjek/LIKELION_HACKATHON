from .views import *
from django.urls import path

app_name='service'

urlpatterns=[
    
    #path('/doctor/main/', DocPage.as_view()),
    #path('/doctor/access/<int:pk>/', DOC_PatNFTPage.as_view()),
    path('doctor/access/medicalinfo/', MediInfo_Write.as_view()),
    path('doctor/access/caution/', Caution_Write.as_view()),
    path('doctor/access/family/', Fam_Write.as_view()),
    path('doctor/access/guardian/', Gua_Write.as_view()),
    path('doctor/access/<int:pk>/medicalinfo/',MediInfoDetailView.as_view()),
    
    
    #path('/doctor/access/<int:pk>/diagnosis/', DOC_DiagnosisList.as_view()),
    #path('/doctor/access/<int:pk>/diagnosis/<int:pk>/', DOC_DiagnosisDetail.as_view()),
    #path('/doctor/access/<int:pk>/medication/', DOC_MedicationList.as_view()),
    #path('/doctor/access/<int:pk>/medication/<int:pk>/', DOC_MedictionDetail.as_view()),
    #path('/doctor/access/<int:pk>/surgery/', DOC_SurgeryList.as_view()),
    #path('/doctor/access/<int:pk>/surgery/<int:pk>/', DOC_SurgeryDetail.as_view()),
    #path('/patient/main/', PatPage.as_view()),
    #path('/patient/access/<int:pk>/medicalinfo/', PAT_MediInfo.as_view()),
    #path('/patient/access/<int:pk>/diagnosis/', PAT_DiagnosisList.as_view()),
    #path('/patient/access/<int:pk>/diagnosis/<int:pk>/', PAT_DiagnosisDetail.as_view()),
    #path('/patient/access/<int:pk>/medication/', PAT_MedicationList.as_view()),
    #path('/patient/access/<int:pk>/medication/<int:pk>/', PAT_MedictionDetail.as_view()),
    #path('/patient/access/<int:pk>/surgery/', PAT_SurgeryList.as_view()),
    #path('/patient/access/<int:pk>/surgery/<int:pk>/', PAT_SurgeryDetail.as_view()),
    #path('/patient/access/<int:pk>/updateRecord/', DOC_UpdateRecord.as_view()),
    #path('/patient/access/<int:pk>/updateRecord/', PAT_UpdateRecord.as_view()),
    #path('/accounts/signup/', SignUp.as_view()),
    #path('/accounts/login/', LogIn.as_view()),
    #path('/accounts/<int:pk>/doctorcertification/', DocCertificate.as_view()),
    #path('/doctor/access/<int:pk>/diagnosis/update/', DOC_diagnosis_update.as_view()),
    #path('/doctor/access/<int:pk>/medication/update/', DOC_medication_update.as_view()),
    #path('/doctor/access/<int:pk>/surgery/update/', DOC_surgery_update.as_view()),
    
]