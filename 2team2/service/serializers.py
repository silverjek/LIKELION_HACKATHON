from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','userType','latestUpdate']

class CautionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caution
        fields = ['id','user_id','info_id','cauLevel','cauName',
                  'cauType','cauSymptom']

class FamHisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fam_History
        fields = ['id','user_id','info_id','famRelation','famDiag',
                  'famBirth','famDeath','famDReason']

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = ['id','user_id','info_id','guaName','guaRelation',
                  'guaPhone']

class MediInfoSerializer(serializers.ModelSerializer):
    caution = CautionSerializer(many=True, read_only=True)
    fam_history = FamHisSerializer(many=True, read_only=True)
    guardian = GuardianSerializer(many=True, read_only=True)
    class Meta:
        model = Medi_Info
        fields = ['id','user_id','patName','patSex','patBirth',
                  'patAddress','patSSN','patBlood','patRH',
                  'patHeight','patWeight','patPhone','updateDate','caution', 'fam_history', 'guardian']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','user_id','docHospital','docMajor','docName',
                  'docSign','docFile']
        
class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['id','user_id','info_id','doc_id','diagDate',
                  'diagRegi','diagNum','diagMajor','diagMajCode',
                  'diagTF','diagMinor','diagMinCode','diagInitDate',
                  'diagMemo','diagIn','diagOut','diagUSage',
                  'diagETC','updateDate']

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id','user_id','info_id','diag_id','pre_id',
                  'mediName','mediEffect','mediDetail','mediCode',
                  'mediUnit','mediAmount','mediCount','mediPeriod']

class PrescriptionSerializer(serializers.ModelSerializer):
    medication = MedicationSerializer(many=True, read_only=True)
    class Meta:
        moel = Prescription
        fields = ['id','user_id','info_id','diag_id','prePharm',
                  'preAddress','preDate','preChem','updateDate']
        
class SurgerySerializer(serializers.ModelSerializer):
    diagnosis = DiagnosisSerializer(many=True, read_only=True)
    mediinfo = MediInfoSerializer(many=True, read_only=True)
    doctor = DoctorSerializer(many=True, read_only=True)
    class Meta:
        model = Surgery
        fields = ['id','user_id','info_id','diag_id','doc_id',
                  'surChartNu','surWriter','surDate','surNum','surHospital',
                  'surField','surOper','surAssi','surAnesDoc','surName',
                  'surCode','surPreDiag','surPostDiag','surAnes','surEvent',
                  'surRemoval','surBloodTrans','surPre','surDur','surPost',
                  'surTube','updateDate']