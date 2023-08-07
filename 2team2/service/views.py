from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response


# Create your views here.
'''
#환자  NFT 접근 시 페이지
class DOC_PatNFTPage(views.APIView):
    def get(self, request, pk, format=None):
        users=get_object_or_404(User, pk=pk) #User 모델 pk
        serializer=UserSerializer(users)
        #User 모델 id, userName, latesUpdate
        return Response(serializer.data)
'''
class MediInfo_Write(views.APIView):
    def post(self, request, format=None):
        medi_serializer=MediInfoSerializer(data=request.data)
        if medi_serializer.is_valid():
            medi_serializer.save()
            return Response(medi_serializer.data)
        return Response( medi_serializer.errors)
    
class Caution_Write(views.APIView):
    def post(self, request, format=None):
        cau_serializer=CautionSerializer(data=request.data)
        if cau_serializer.is_valid():
            cau_serializer.save()
            return Response(cau_serializer.data)
        return Response( cau_serializer.errors)

class Fam_Write(views.APIView):
    def post(self, request, format=None):
        fam_serializer=FamHisSerializer(data=request.data)
        if fam_serializer.is_valid():
            fam_serializer.save()
            return Response(fam_serializer.data)
        return Response( fam_serializer.errors)

class Gua_Write(views.APIView):
    def post(self, request, format=None):
        gua_serializer=GuardianSerializer(data=request.data)
        if gua_serializer.is_valid():
            gua_serializer.save()
            return Response(gua_serializer.data)
        return Response( gua_serializer.errors)
    
#환자 의료정보 상세조회

class MediInfoDetailView(views.APIView):
    def get(self, request, pk,  format=None):
        mediinfo=get_object_or_404(Medi_Info, pk=pk) #Medi_info 모델 pk
        caution=get_object_or_404(Caution, pk=pk)
        famhistory=get_object_or_404(Fam_History, pk=pk)
        guardian=get_object_or_404(Guardian, pk=pk)

        medi_serializer=MediInfoSerializer(mediinfo)
        cau_serializer=CautionSerializer(caution)
        fam_serializer=FamHisSerializer(famhistory)
        gua_serializer=GuardianSerializer(guardian)

        combined_data={
            'medi':medi_serializer.data,
            'cau':cau_serializer.data,
            'fam':fam_serializer.data,
            'gua':gua_serializer.data
        }
        #Caution 모델의 id, cauMedicine, cauLevel, cauName, cauType, cauSymptom
        #Fam_History 모델의 id, info_id, famDiag, famRelation, famBirth, famDeath,, famDReason
        #Guardian 모델의 id, info_id, guaName, guaRelation, guaPhone
        return Response(combined_data)
'''
#환자 진료내역 조회 - 진단 리스트   
class DOC_DiagnosisList(views.APIView):
    def get(self, request, pk, format=None):
        diagnosises=get_object_or_404(Diagnosis, pk=Medi_Info.id) #Medi_info 모델 pk
        serializer=DiagnosisSerializer(diagnosises)
        #Diagnosis 모델의 id, diagHospital, diagDate, diagDoc, diagName, diagCode, diagLoc
        return Response(serializer.data)

#상세 진단기록 조회
class DOC_DiagnosisDetail(views.APIView):
    def get(self, requestk, pk, formay=None):
        diagnosisdetails=get_object_or_404() #Medi_Info 모델 pk, Diagnosis 모델 pk
        #Medi_info 모델 id
        #Diagnosis 모델 id, updateDate, diag,Date, diagRegi, diagNum, diagMajor, diagMajCode, diagTF, diagMinor, diagMinCode, diagInitDate, diagDate, diagMemo, diagIn, diagOut, diagUsage, diagETC
        #Doctor 모델 id, docName, docHospital
        #Medi_info 모델 id, patName, patSSN, patAge, patSex, patPhone, patAddress

#환자 진료내역 조회 - 약물처방 리스트
class DOC_MedicationList(views.APIView):
    def get(self, request, pk, format=None):
        medications=get_object_or_404(Medication, pk=Medi_Info.id)
        serializer=PrescriptionSerializer(medications)
        #Medi_info 모델 id
        #Prescription 모델 id, prePharm, preAddress, preChem, preDate
        return Response(serializer.data)

#상세 약물처방 조회
class DOC_MedictionDetail(views.APIView):
    def get(self, request, pk, format=None):
        #Medi_Info 모델 id
        #Prescription 모델 id, preDate, prePharm, preAddress, preChem
        #Diagnosis 모델 id
        #Medication 모델 id, mediName, mediEffect, mediDetail, mediCode, mediUnit, mediAmount, mediCount, mediPeriod



#환자 진료내역 조회 - 수술 리스트
class DOC_SurgeryList(views.APIView):
    def get(self, request, pk, format=None):
        surgeries=get_object_or_404(Surgery, pk=Medi_Info.id) #Medi_Info 모델 pk
        serializer=SurgerySerializer(surgeries)
        #Diagnosis 모델의 id, diagHospital, diagDate, diagName, diagCode, diagDoc
        #Surgery 모델의 id, surDate, surName, surCode, surDoc
        return Response(serializer.data)
    
#상세 수술기록 조회
class DOC_SurgeryDetail(views.APIView):
    def get(self, request, pk, format=None):
        #Medi_Info 모델 pk
        #Surgery 모델 pk
        #Surgery 모델 surChartNum, updateDate, surWriter, surDate, surNum, surHospital, surField, surOper, surAssi, surAnesDoc, surName,surCode, surPreDiag, surPostDiag, surAnes, surEvent, surRemoval, surBloodTrans, surPre, surDur, surPost, surTube
        #Diag 모델 id, diagDate, diagName, diagCode, diagDoc, diagHospital
        #Medi_Info 모델 patName, patSSN, patAge, patSex, patPhone
        #Doctor 모델 id, docSign

#의사 랜딩 페이지(승인된 NFT 리스트)
class DocPage(views.APIView): 
    def get(self,format=None):
        #info_id, patName, approveDate 

#환자 랜딩 페이지 
class PatPage(views.APIView):
    def get(self,format=None):
        # User 모델 pk
        #user_id, patName, updateDate

#본인 의료정보 상세조회 
class PAT_MediInfo(views.APIView):
    def get(self, request, pk, format=None):
        mediinfo=get_object_or_404(Medi_Info, pk=User.id) #User 모델 pk
        serializer=MediInfoSerializer(mediinfo)
        #User 모델 pk
        #Medi_Info 모델 pk, patName, patSex, patBirth, patSSN, patBlood, patRH, patHeight, patWeight, patPhone, patAddress
        #Caution 모델 pk, cauMedicine, cauLevel, cauName, cauType, cauSymptom
        #Fam_History 모델 pk, famDiag, famRelation, famBirth, famDeath, famDReason
        #Guardian 모델 pk, guaName, guaRelation, guaPhone
        #
        return Response(serializer.data)

#본인 진료내역 조회 - 진단 리스트
class PAT_DiagnosisList(views.APIView):
    def get(self, request, pk, format=None):
        diagnosises=get_object_or_404(Diagnosis, pk=User.id) #User 모델 pk
        serializer=DiagnosisSerializer(diagnosises)
        #Diagnosis 모델의 id, diagHospital, diagDate, diagDoc, diagName, diagCode, diagLoc
        return Response(serializer.data)

#상세 진단기록 조회
class PAT_DiagnosisDetail(views.APIView):
    def get(self, requestk, pk, formay=None):
        #User 모델 pk
        ##Diagnosis 모델 id, updateDate, diag,Date, diagRegi, diagNum, diagMajor, diagMajCode, diagTF, diagMinor, diagMinCode, diagInitDate, diagDate, diagMemo, diagIn, diagOut, diagUsage, diagETC
        #Doctor 모델 id, docName, docHospital
        #Medi_info 모델 id, patName, patSSN, patAge, patSex, patPhone, patAddress
        diagnosisdetails=get_object_or_404()

#본인 진료내역 조회 - 약물처방 리스트  
class PAT_MedicationList(views.APIView):
    def get(self, request, pk, format=None):
        medications=get_object_or_404(Medication, pk=User.id) #User 모델 pk
        serializer=PrescriptionSerializer(medications)
        #Prescription 모델 id, prePharm, preAddress, preChem, preDate
        return Response(serializer.data)

#상세 약물처방 조회
class PAT_MedictionDetail(views.APIView):
    def get(self, request, pk, format=None):
        #User 모델 pk
        #Prescription 모델 id, preDate, prePharm, preAddress, preChem
        #Diagnosis 모델 id
        #Medication 모델 id, mediName, mediEffect, mediDetail, mediCode, mediUnit, mediAmount, mediCount, mediPeriod


#본인 진료내역 조회 - 수술 리스트
class PAT_SurgeryList(views.APIView):
    def get(self, request, pk, format=None):
        surgeries=get_object_or_404(Surgery, pk=User.id) #User 모델 pk
        serializer=SurgerySerializer(surgeries)
        #Diagnosis 모델의 id, diagHospital, diagDate, diagName, diagCode, diagDoc
        #Surgery 모델의 id, surDate, surName, surCode, surDoc
        return Response(serializer.data)

#상세 수술기록 조회
class PAT_SurgeryDetail(views.APIView):
    def get(self, request, pk, format=None):
        #User 모델 pk
        #Surgery 모델 pk
        #Surgery 모델 surChartNum, updateDate, surWriter, surDate, surNum, surHospital, surField, surOper, surAssi, surAnesDoc, surName,surCode, surPreDiag, surPostDiag, surAnes, surEvent, surRemoval, surBloodTrans, surPre, surDur, surPost, surTube
        #Diag 모델 id, diagDate, diagName, diagCode, diagDoc, diagHospital
        #Medi_Info 모델 patName, patSSN, patAge, patSex, patPhone
        #Doctor 모델 id, docSign


#의사 - NFT 갱신 기록 
class DOC_UpdateRecord(views.APIView):
    def get(self, request, pk, format=None):
        #Medi_Info 모델 pk, updateDate
        #Diagnosis 모델 pk, diagHospital, updateDate, diagDoc
        #Surgery 모델 pk, surHospital, updateDate, surOperator
        #Medication 모델 pk, updateDate

#환자 - NFT 갱신 기록 
class PAT_UpdateRecord(views.APIView):
    def get(self, request, pk, format=None):
        #User 모델 pk
        #Medi_Info 모델 id, updateDate
        #Diagnosis 모델 id, diagHospital, updateDate, diagDoc
        #Surgery 모델 id, surHospital, updateDate, surOperator
        #Medication 모델 id, updateDate

class SignUp(views.APIView):
    def get():

class LogIn(views.APIView):
    def post():

class DocCertificate(views.APIView):
    def post():

class DOC_diagnosis_update(views.APIView):
    def post():

class DOC_medication_update(views.APIView):
    def post():

class DOC_surgery_update(views.APIView):
    def post():
'''
