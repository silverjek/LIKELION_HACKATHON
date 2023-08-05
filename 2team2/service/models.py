from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(AbstractUser):
    password = models.CharField(max_length=20) #기본 8자 이상의 규칙이 있어 minimum 설정은 건너뛰었습니다
    userType = models.BooleanField(default=True) #True-일반사용자 / False-의료인사용자
    latestUpdate = models.DateTimeField(null=True, blank=True)
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
    patAddress = models.CharField(max_length=100)
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
    updateDate = models.DateTimeField(auto_now_add=True)
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

class Doctor(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    docHospital = models.CharField(max_length=100)
    docMajor = models.CharField(max_length=100)
    docName = models.CharField(max_length=20)
    docSign = models.ImageField()
    docFile = models.ImageField()

class Diagnosis(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    info_id = models.ForeignKey(Medi_Info, on_delete=models.CASCADE)
    doc_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    updateDate = models.DateTimeField(auto_now_add=True)
    diagDate = models.DateField()
    diagRegi = models.CharField(max_length=50)
    diagNum = models.CharField(max_length=50)
    diagMajor = models.CharField(max_length=100)
    diagMajCode = models.CharField(max_length=100)
    diagTF = models.BooleanField(default=False) #False-임상적 추정 / True-최종 진단
    diagMinor = models.CharField(max_length=300)
    diagMinCode = models.CharField(max_length=300)
    diagInitDate = models.DateField()
    diagMemo = models.TextField
    diagIn = models.DateField()
    diagOut = models.DateField()
    diagUSage = models.CharField(max_length=50, blank=True, null=True)
    diagETC = models.TextField() #api 명세서에 char로 해두었는데 비고면 무슨 내용이 어떻게 들어갈지 몰라 text가 나을 것 같아 바꿨습니다..