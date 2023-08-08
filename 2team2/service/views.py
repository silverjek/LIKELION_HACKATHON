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

        #Caution 모델의 id, cauMedicine, cauLevel, cauName, cauType, cauSymptom
        #Fam_History 모델의 id, info_id, famDiag, famRelation, famBirth, famDeath,, famDReason
        #Guardian 모델의 id, info_id, guaName, guaRelation, guaPhone
        return Response(combined_data)

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