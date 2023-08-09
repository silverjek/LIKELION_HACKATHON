from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response


# Create your views here.

'''
<백엔드 자체 관리용> -----------------------------------------------------
'''
#의사 정보등록
class Doctor_Write(views.APIView):
    def post(self, request, format=None):
        doc_serializer=DoctorSerializer(data=request.data)
        if doc_serializer.is_valid():
            doc_serializer.save()
            return Response(doc_serializer.data)
        return Response(doc_serializer.errors)

#기본의료 정보등록
class MediInfo_Write(views.APIView):
    def post(self, request, format=None):
        medi_serializer=MediInfoSerializer(data=request.data)
        if medi_serializer.is_valid():
            medi_serializer.save()
            return Response(medi_serializer.data)
        return Response(medi_serializer.errors)

#알러지/부작용 정보등록     
class Caution_Write(views.APIView):
    def post(self, request, format=None):
        cau_serializer=CautionSerializer(data=request.data)
        if cau_serializer.is_valid():
            cau_serializer.save()
            return Response(cau_serializer.data)
        return Response(cau_serializer.errors)

#가족력 정보등록
class FamHis_Write(views.APIView):
    def post(self, request, format=None):
        fam_serializer=FamHisSerializer(data=request.data)
        if fam_serializer.is_valid():
            fam_serializer.save()
            return Response(fam_serializer.data)
        return Response(fam_serializer.errors)

#보호자 정보등록
class Guardian_Write(views.APIView):
    def post(self, request, format=None):
        gua_serializer=GuardianSerializer(data=request.data)
        if gua_serializer.is_valid():
            gua_serializer.save()
            return Response(gua_serializer.data)
        return Response(gua_serializer.errors)
    
#진단 정보등록
class Diagnosis_Write(views.APIView):
    def post(self, request, format=None):
        diag_serializer=DiagnosisSerializer(data=request.data)
        if diag_serializer.is_valid():
            diag_serializer.save()
            return Response(diag_serializer.data)
        return Response(diag_serializer.errors)

#처방 정보등록    
class Prescription_Write(views.APIView):
    def post(self, request, format=None):
        pre_serializer=PrescriptionSerializer(data=request.data)
        if pre_serializer.is_valid():
            pre_serializer.save()
            return Response(pre_serializer.data)
        return Response(pre_serializer.errors)
    
#약 정보등록    
class Medication_Write(views.APIView):
    def post(self, request, format=None):
        pre_serializer=PrescriptionSerializer(data=request.data)
        if pre_serializer.is_valid():
            pre_serializer.save()
            return Response(pre_serializer.data)
        return Response(pre_serializer.errors)

#수술 정보등록    
class Surgery_Write(views.APIView):
    def post(self, request, format=None):
        sur_serializer=SurgerySerializer(data=request.data)
        if sur_serializer.is_valid():
            sur_serializer.save()
            return Response(sur_serializer.data)
        return Response(sur_serializer.errors)
    
'''
<회원가입/로그인> ------------------------------------------------------------------
'''

class SignUpView(views.APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'회원가입 성공', 'data':serializer.data})
        return Response({'message':'회원가입 실패', 'error':serializer.errors})

class LoginView(views.APIView):
    def post(self, request):
        serializer=UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response({'message':'로그인 성공', 'data':serializer.data})
        return Response({'message':'로그인 실패', 'error':serializer.errors})
    
'''
<의사> ------------------------------------------------------------------
'''

#의사_의료정보 상세조회
class MediInfoDetailView(views.APIView):
    def get(self, request, pk, format=None):
        mediinfo = get_object_or_404(Medi_Info, pk=pk)  # Medi_info 모델 pk
        cautions = Caution.objects.filter(info_id=pk)
        famhistories = Fam_History.objects.filter(info_id=pk)
        guardians = Guardian.objects.filter(info_id=pk)

        medi_serializer = MediInfoSerializer(mediinfo)
        cau_serializers = [CautionSerializer(caution) for caution in cautions]
        fam_serializers = [FamHisSerializer(famhistory) for famhistory in famhistories]
        gua_serializers = [GuardianSerializer(guardian) for guardian in guardians]

        combined_data = {
            'medi': medi_serializer.data,
            'cau': [cau_serializer.data for cau_serializer in cau_serializers],
            'fam': [fam_serializer.data for fam_serializer in fam_serializers],
            'gua': [gua_serializer.data for gua_serializer in gua_serializers]
        }

        return Response(combined_data)

#의사_진단 리스트
class DiagnosisListView(views.APIView):
    def get(self, request, pk, format=None):
        diags = Diagnosis.objects.all(info_id=pk)
        serializer = DiagnosisSerializer(diags, many=True) #필드 제한 필요
        return Response(serializer.data)
    
#의사_진단 상세조회
class DiagnosisDetailView(views.APIView):
    def get(self, request, first_pk, second_pk, format=None):
        mediinfo = get_object_or_404(Medi_Info, pk=first_pk)  # Medi_info 모델 pk
        diagnosiss = Caution.objects.filter(id=second_pk)

        medi_serializer = MediInfoSerializer(mediinfo)
        diag_serializers = [DiagnosisSerializer(diagnosis) for diagnosis in diagnosiss]
        
        combined_data = {
            'medi': medi_serializer.data,
            'diag': [diag_serializer.data for diag_serializer in diag_serializers]
        }

        return Response(combined_data)

#의사_약물처방 리스트
class PrescriptionListView(views.APIView):
    def get(self, request, pk, format=None):
        pres = Prescription.objects.all(info_id=pk)
        serializer = PrescriptionSerializer(pres, many=True) #필드 제한 필요
        return Response(serializer.data)
    
#의사_약물처방 상세조회
class PrescriptionDetailView(views.APIView):
    def get(self, request, first_pk, second_pk, format=None):
        mediinfo = get_object_or_404(Medi_Info, pk=first_pk)  # Medi_info 모델 pk
        #prescriptions = Caution.objects.filter(pk=second_pk)
        prescriptions = get_object_or_404(Prescription, pk=first_pk)
        medications = Medication.objects.filter(pre_id=second_pk) #얘 pk 이렇게 받는게 맞나..?

        medi_serializer = MediInfoSerializer(mediinfo)
        pre_serializers = [PrescriptionSerializer(prescription) for prescription in prescriptions]
        med_serializers = [MedicationSerializer(medication) for medication in medications]
        
        combined_data = {
            'medi': medi_serializer.data,
            'pre': [pre_serializer.data for pre_serializer in pre_serializers],
            'med': [med_serializer.data for med_serializer in med_serializers]
        }

        return Response(combined_data)

#의사_수술 리스트
class SurgeryListView(views.APIView):
    def get(self, request, pk, format=None):
        surs = Surgery.objects.all(info_id=pk)
        serializer = SurgerySerializer(surs, many=True) #필드 제한 필요
        return Response(serializer.data)
    
#의사_수술 상세조회
class SurgeryDetailView(views.APIView):
    def get(self, request, first_pk, second_pk, format=None):
        mediinfo = get_object_or_404(Medi_Info, pk=first_pk)  # Medi_info 모델 pk
        #surgery = Surgery.objects.filter(info_id=first_pk, id=second_pk)
        surgerys = get_object_or_404(Surgery, pk=second_pk)
        diagnosiss = Diagnosis.objects.filter(id=surgerys.diag_id)

        medi_serializer = MediInfoSerializer(mediinfo)
        sur_serializers = [SurgerySerializer(surgery) for surgery in surgerys]
        diag_serializers = [DiagnosisSerializer(diagnosis) for diagnosis in diagnosiss]
        
        
        combined_data = {
            'medi': medi_serializer.data,
            'sur': [sur_serializer.data for sur_serializer in sur_serializers],
            'diag': [diag_serializer.data for diag_serializer in diag_serializers]
        }

        return Response(combined_data)
