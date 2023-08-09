from .views import *
from django.urls import path

app_name='service'

urlpatterns=[
    
    #path('/doctor/main/', DocPage.as_view()),
    #path('/doctor/access/<int:pk>/', DOC_PatNFTPage.as_view()),
    path('manage/write/doctor/', Doctor_Write.as_view()),
    path('manage/write/mediinfo/', MediInfo_Write.as_view()),
    path('manage/write/caution/', Caution_Write.as_view()),
    path('manage/write/famhis/', FamHis_Write.as_view()),
    path('manage/write/guardidan/', Guardian_Write.as_view()),
    path('manage/write/diagnosis/', Diagnosis_Write.as_view()),
    path('manage/write/prescription/', Prescription_Write.as_view()),
    path('manage/write/medication/', Medication_Write.as_view()),
    path('manage/write/surgery/', Surgery_Write.as_view()),
    
    path('doctor/access/<int:pk>/medicalinfo/',DOC_MediInfoDetailView.as_view()),
    path('doctor/access/<int:pk>/diagnosis/',DOC_DiagnosisListView.as_view()),
    path('doctor/access/<int:first_pk>/diagnosis/<int:second_pk>/',DOC_DiagnosisDetailView.as_view()),
    path('doctor/access/<int:pk>/medication/',DOC_PrescriptionListView.as_view()),
    path('doctor/access/<int:first_pk>/medication/<int:second_pk>/',DOC_PrescriptionDetailView.as_view()),
    path('doctor/access/<int:pk>/surgery/',DOC_SurgeryListView.as_view()),
    path('/doctor/access/<int:first_pk>/surgery/<int:second_pk>/',DOC_SurgeryDetailView.as_view()),
    #path('patient/access/<int:pk>/medicalinfo/',PAT_MediInfoDetailView.as_view()),
    
    
]