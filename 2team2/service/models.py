from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20) #기본 8자 이상의 규칙이 있어 minimum 설정은 건너뛰었습니다
    userType = models.BooleanField(default=True) #True-일반사용자 / False-의료인사용자
    

    #userName --- 아이디, 비밀번호, 이름은 기본 필드가 존재
    #userSSN --- 이 아래로 User 모델의 정보를 실사용하는 경우가 없음
    #userPhone
    #userEmail
    #userAddress
    #userPatient

class Medi_Info(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    patName = models.CharField(max_length=30)
    SEX_CHOICES=(
        ('FEMALE','Female'),
        ('MALE','Male')
    )
    patSex = models.CharField(max_length=6, choices=SEX_CHOICES)
    patBirth = models.DateField()
    patAddress = models.CharField(max_length=200)
    patSSN = models.CharField(max_length=14)
    BLOOD_CHOICES=(
        ('A','A'),
        ('B','B'),
        ('O','o'),
        ('AB','AB')
    )
    patBlood = models.CharField(max_length=2, choices=BLOOD_CHOICES)
    RH_CHOICES=(
        ('PLUS','+'),
        ('MINUS','-')
    )
    patRH = models.CharField(max_length=5, choices=RH_CHOICES)
    patHeight = models.FloatField()
    patWeight = models.FloatField()
    patPhone = PhoneNumberField(unique=True, null=False, blank=False) #unique 설정을 풀어야할지도.. 의료인의 경우 환자로 또 가입하려면 한 번호로 두번 가입해야하니까
    updateDate = models.DateTimeField(auto_now_add=True) #의료기록 자체 갱신날짜
    #latestUpdate = models.DateTimeField(null=True, blank=True)
    #approveDate = models.DateTimeField() --- erd에는 있는데 api명세서에는 없어서 일단 빼두었습니다

class Caution(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    LEVEL_CHOICES = (
        ('SEVERE','Severe'),
        ('MODERATE','Moderate'),
        ('MILD','Mild')
    )
    cauLevel = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    cauName = models.CharField(max_length=300) #장고에 varchar필드가 따로 없고 Char 필드가 sql에서 varchar로 변환된다 합니다..
    cauType = models.CharField(max_length=300)
    cauSymptom = models.CharField(max_length=300)

class Fam_History(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    famRelation = models.CharField(max_length=100)
    famDiag = models.CharField(max_length=100)
    famBirth = models.DateField()
    famDeath = models.DateField(blank=True, null=True)
    famDReason = models.CharField(max_length=50, blank=True, null=True)

class Guardian(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    guaName = models.CharField(max_length=20)
    guaRelation = models.CharField(max_length=100)
    guaPhone = PhoneNumberField(unique=True, null=False, blank=False)

'''
class Doctor(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    docHospital = models.CharField(max_length=100)
    docMajor = models.CharField(max_length=100)
    docName = models.CharField(max_length=20)
    docSign = models.ImageField(blank=True, null=True)
    docFile = models.ImageField(blank=True, null=True)
'''
class Diagnosis(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    diagDate = models.DateField()
    diagRegi = models.CharField(max_length=50)
    diagNum = models.CharField(max_length=50)
    diagMajor = models.CharField(max_length=100)
    diagMajCode = models.CharField(max_length=100)
    diagTF = models.BooleanField(default=False) #False-임상적 추정 / True-최종 진단
    diagMinor = models.CharField(max_length=300)
    diagMinCode = models.CharField(max_length=300)
    diagInitDate = models.DateField()
    diagMemo = models.TextField(null=False, blank=False, default='')
    diagIn = models.DateField()
    diagOut = models.DateField()
    diagUSage = models.CharField(max_length=50, blank=True, null=True)
    diagETC = models.TextField(null=False, blank=False, default='') #api 명세서에 char로 해두었는데 비고면 무슨 내용이 어떻게 들어갈지 몰라 text가 나을 것 같아 바꿨습니다..
    updateDate = models.DateTimeField(auto_now_add=True)
    #docName = models.CharField(max_length=20, null=True, blank=True)
    #docHospital = models.CharField(max_length=100, null=True, blank=True)

class Prescription(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    diag_id = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    prePharm = models.CharField(max_length=100)
    preAddress = models.CharField(max_length=200)
    preDate = models.DateField()
    preChem = models.CharField(max_length=20)
    updateDate = models.DateTimeField(auto_now_add=True)
    #approveDate = models.DateTimeField() --- erd에는 있는데 api명세서에는 없어서 일단 빼두었습니다

class Medication(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    diag_id = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    pre_id = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    mediName = models.CharField(max_length=100)
    mediEffect = models.CharField(max_length=300)
    mediDetail = models.CharField(max_length=100)
    mediCode = models.CharField(max_length=100)
    mediUnit = models.CharField(max_length=50)
    mediAmount = models.CharField(max_length=50)
    mediCount = models.CharField(max_length=50)
    mediPeriod = models.CharField(max_length=50)

class Surgery(models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    diag_id = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    surChartNum = models.CharField(max_length=50)
    surWriter = models.CharField(max_length=20)
    surDate = models.DateField()
    surNum = models.IntegerField()
    surHospital = models.CharField(max_length=100)
    surField = models.CharField(max_length=300)
    surOper = models.CharField(max_length=20)
    surAssi = models.CharField(max_length=20)
    surAnesDoc = models.CharField(max_length=20)
    surName = models.CharField(max_length=100)
    surCode = models.CharField(max_length=50)
    surPreDiag = models.CharField(max_length=100)
    surPostDiag = models.CharField(max_length=100)
    surAnes = models.CharField(max_length=100)
    surEvent = models.BooleanField(default=False) #False-무 / True-유
    surRemoval = models.BooleanField(default=False) #False-무 / True-유
    surBloodTrans = models.BooleanField(default=False) #False-무 / True-유
    surPre = models.TextField(null=False, blank=False, default='')
    surDur = models.TextField(null=False, blank=False, default='')
    surPost = models.TextField(null=False, blank=False, default='')
    surTube = models.BooleanField(default=False) #False-무 / True-유
    updateDate = models.DateTimeField(auto_now_add=True)
    #docSign = models.ImageField()
    #approveDate = models.DateTimeField() --- erd에는 있는데 api명세서에는 없어서 일단 빼두었습니다
