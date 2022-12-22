from django.db import models
from django.db.models import Count
from django.db import models
from django_jalali.db import models as jmodels
from django_jalali.db.models import jDateField
from django.contrib.auth.models import AbstractUser, UserManager,AbstractBaseUser
from django_jalali.admin.widgets import AdminjDateWidget


from django.db import models
from django.utils import timezone
import datetime



# Create your models here.  
from .managers import UserManager

class OP1(models.Model):
    
    absrob_response_choices= [
        ('مسئول جذب 1', 'مسئول جذب 1'),
    ('مسئول جذب 2', 'مسئول جذب 2'),
    ('مسئول جذب 3', 'مسئول جذب 3'),
] 
    
    biker_edu_choices=[
   ('کارشناس 1 ', ' کارشناس 1'),
('کارشناس 2 ', ' کارشناس 2'),
('کارشناس 3 ', ' کارشناس 3'),
('کارشناس 4 ', ' کارشناس 4'),
('کارشناس 5 ', ' کارشناس 5'),
('کارشناس 6 ', ' کارشناس 6'),
('کارشناس 7 ', ' کارشناس 7'),
('کارشناس 8 ', ' کارشناس 8'),
                    
                    ]   
    
    vehicle_choices = [
 
    ('خودرو', 'خودرو'),
    ('موتورسیکلت', 'موتورسیکلت'),
       ('موتورسیکلت /خودرو', 'موتورسیکلت /خودرو'),
    ('وانت', 'وانت'),
] 
    
    contract_type_choices = [
   
    ('استخدامی', 'استخدامی'),
    ('پیمانی', 'پیمانی'),

]    

    status_choices = [

    ('منفی', 'منفی'),
    ('مثبت', 'مثبت'),
    ('بی پاسخ', 'بی پاسخ'),

    ('ورود به دفتر', 'ورود به دفتر'),
]  
    
    company_name_choices = [

    ('اکالا', 'اکالا'),
    ('افق کوروش', 'افق کوروش'),
]     
  
  
    branch_choices = [


("تهران جنوب شرق", "تهران جنوب شرق"),
("تهران جنوب غرب", "تهران جنوب غرب"),
("تهران شمال شرق", "تهران شمال شرق"),
("تهران شمال غرب", "تهران شمال غرب"),
("شعبه استان فارس", "شعبه استان فارس"),
("شعبه استان اصفهان", "شعبه استان اصفهان"),
("شعبه استان لرستان", "شعبه استان لرستان"),
("شعبه استان کرمانشاه", "شعبه استان کرمانشاه"),
("شعبه استان گيلان", "شعبه استان گيلان"),
("شعبه کرمانشاه 2", "شعبه کرمانشاه 2"),
("شعبه مازندران2", "شعبه مازندران2"),
("شعبه استان سمنان", "شعبه استان سمنان"),
("شعبه استان کرمان", "شعبه استان کرمان"),
(" استان البرز2", " استان البرز2"),
("شعبه استان مازندران", "شعبه استان مازندران"),
("شعبه استان همدان", "شعبه استان همدان"),
("شعبه استان آذربايجان غربي", "شعبه استان آذربايجان غربي"),
("شعبه آذربايجان شرقي2", "شعبه آذربايجان شرقي2"),
("شعبه استان خوزستان", "شعبه استان خوزستان"),
("شعبه استان خراسان رضوي", "شعبه استان خراسان رضوي"),
("استان خوزستان 2", "استان خوزستان 2"),
("شعبه استان قزوين", "شعبه استان قزوين"),
("شعبه استان ايلام", "شعبه استان ايلام"),
("شعبه استان خراسان شمالي", "شعبه استان خراسان شمالي"),
(" شعبه استان قم", " شعبه استان قم"),
("شعبه استان البرز", "شعبه استان البرز"),
("شعبه استان بوشهر", "شعبه استان بوشهر"),
("شعبه استان کردستان", "شعبه استان کردستان"),
("شعبه گيلان2", "شعبه گيلان2"),
("شعبه استان هرمزگان", "شعبه استان هرمزگان"),
("شعبه استان اردبيل", "شعبه استان اردبيل"),
("شعبه استان آذربايجان شرقي", "شعبه استان آذربايجان شرقي"),
("شعبه استان خراسان جنوبي", "شعبه استان خراسان جنوبي"),
("شعبه يزد 2", "شعبه يزد 2"),
("شعبه استان گلستان", "شعبه استان گلستان"),
("شعبه استان چهارمحال و بختياري", "شعبه استان چهارمحال و بختياري"),
("شعبه استان يزد", "شعبه استان يزد"),
("شعبه استان مرکزي", "شعبه استان مرکزي"),
("شعبه استان زنجان", "شعبه استان زنجان"),
("شعبه استان کهکيلويه و بويراحمد", "شعبه استان کهکيلويه و بويراحمد"),
("شعبه استان سيستان و بلوچستان", "شعبه استان سيستان و بلوچستان"),
    
]   
    
    city_choices = [

("تهران","تهران"),
("مشهد","مشهد"), 
("اهواز","اهواز"),
("شيراز","شيراز"),
("اصفهان","اصفهان"),
("قم","قم"),
("قزوين","قزوين"),
("اسلامشهر","اسلامشهر"),
("کرج","کرج"),
("تبريز","تبريز"),
("همدان","همدان"),
("بيرجند","بيرجند"),
("کرمانشاه","کرمانشاه"),
("اردبيل","اردبيل"),
("اروميه","اروميه"),
("رشت","رشت"),
("گنبد كاووس","گنبد كاووس"),
("بابل","بابل"),
("گرگان","گرگان"),
("يزد","يزد"),
("اراک","اراک"),
("پرند","پرند"),
("خرم آباد","خرم آباد"),
("بجنورد","بجنورد"),
("زاهدان","زاهدان"),
("قرچک","قرچک"),
("مرند","مرند"),
("نيشابور","نيشابور"),
("زنجـان","زنجـان"),
("پرديس","پرديس"),
("ايلام","ايلام"),
("شاهرود","شاهرود"),
("سمنان","سمنان"),
("کاشمر","کاشمر"),
("نسيم شهر","نسيم شهر"),
("سنندج","سنندج"),
("ساري","ساري"),
("بروجرد","بروجرد"),
("سقز","سقز"),
("شهر قدس","شهر قدس"),
("پاکدشت","پاکدشت"),
("شوشتر","شوشتر"),
("گلبهار","گلبهار"),
("کاشان","کاشان"),
("گناوه","گناوه"),
("ساوه","ساوه"),
("مراغه","مراغه"),
("صدرا","صدرا"),
("شاهين شهر","شاهين شهر"),
("قائن","قائن"),
("بومهن","بومهن"),
("ملاير","ملاير"),
("ورامين","ورامين"),
("تربت حيدريه","تربت حيدريه"),
("دهدشت","دهدشت"),
("شيروان","شيروان"),
("نورآباد ممسني","نورآباد ممسني"),
("خوي","خوي"),
("بهارستان","بهارستان"),
("خرمشهر","خرمشهر"),
("کازرون","کازرون"),
("تربت جام","تربت جام"),
("ماهشهر","ماهشهر"),
("اندیشه","اندیشه"),
("مسجد سليمان","مسجد سليمان"),
("خواف","خواف"),
("لنگرود","لنگرود"),
("آبادان","آبادان"),
("کلاچاي","کلاچاي"),
("قوچان","قوچان"),
("ياسوج","ياسوج"),
("جهرم","جهرم"),
("مهاباد","مهاباد"),
("ايذه","ايذه"),
("كوهدشت","كوهدشت"),
("برازجان","برازجان"),
("شوش","شوش"),
("شهر کرد","شهر کرد"),
("گچساران","گچساران"),
("لاهيجان","لاهيجان"),
("اسلام آباد غرب","اسلام آباد غرب"),
("درود","درود"),
("بوشهر","بوشهر"),
("ميانه","ميانه"),
("اهر","اهر"),
("انديمشك","انديمشك"),
("انزلي","انزلي"),
("رفسنجان","رفسنجان"),
("لار","لار"),
("بابلسر","بابلسر"),
("آمل","آمل"),
("اردبیل","اردبیل"),
("بوكان","بوكان"),
("سپاهان شهر","سپاهان شهر"),
("اسفراين","اسفراين"),
("پارس آباد","پارس آباد"),
("رودسر","رودسر"),
("انـزلـي","انـزلـي"),

]
    
    description_choices=[

("اتباع ","اتباع "),
("درخواست بیمه -مدارک لازم ندارد","درخواست بیمه -مدارک لازم ندارد"), 
("وسیله نقلیه مورد نظر را ندارد","وسیله نقلیه مورد نظر را ندارد"),
("انصراف(ساعت کاری)","انصراف(ساعت کاری)"),
("انصراف(درآمد کم)","انصراف(درآمد کم)"),
("کسری مدارک(امکان تکمیل ندارد)","کسری مدارک(امکان تکمیل ندارد)"),
("سن متقاضی بالای 50 یا زیر 16","سن متقاضی بالای 50 یا زیر 16"),
("ساکن شهر دیگر","ساکن شهر دیگر"),
("سایر","سایر"),      ]  
    
    description_choices_2=[

("اتباع ","اتباع "),
("درخواست بیمه -مدارک لازم ندارد","درخواست بیمه -مدارک لازم ندارد"), 
("وسیله نقلیه مورد نظر را ندارد","وسیله نقلیه مورد نظر را ندارد"),
("انصراف(ساعت کاری)","انصراف(ساعت کاری)"),
("انصراف(درآمد کم)","انصراف(درآمد کم)"),
("کسری مدارک(امکان تکمیل ندارد)","کسری مدارک(امکان تکمیل ندارد)"),
("سن متقاضی بالای 50 یا زیر 16","سن متقاضی بالای 50 یا زیر 16"),
(" در آینده مراجعه میکند(دلیل در توضیحات) "," در آینده مراجعه میکند(دلیل در توضیحات) "),
(" عدم مراجعه "," عدم مراجعه "),
("کسری مدارک(به زودی تکمیل و مراجعه میکند)  ","کسری مدارک(به زودی تکمیل و مراجعه میکند)  "),
("مردود(ظاهر-رفتار-توانائی)  ","مردود(ظاهر-رفتار-توانائی)  "),
("ساکن شهر دیگر","ساکن شهر دیگر"),
("سایر","سایر"),      ]
    
    name=models.CharField(max_length=100,verbose_name='نام ')
    family=models.CharField(max_length=100,verbose_name=' نام خانوادگی  ')
    nationalCode=models.CharField(max_length=100,null=True,blank=True,verbose_name=' کد ملی  ')
    nationalCodeAttach=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True)
    phone_number=models.BigIntegerField(verbose_name=' شماره موبایل کارکرد1  ')
    phone_number2=models.CharField(max_length=100,null=True,blank=True,verbose_name=' شماره موبایل کارکرد2  ')
    branch=models.CharField(max_length=100,null=True,blank=True,choices=branch_choices,verbose_name='شعبه ')
    age=models.BigIntegerField(null=True,blank=True  ,verbose_name='سن ')
    contractType=models.CharField(max_length=100,null=True,blank=True,choices=contract_type_choices ,verbose_name='نوع قرارداد ')
    vehicle=models.CharField(max_length=100,null=True,blank=True,choices=vehicle_choices ,verbose_name='وسیله نقلیه ')
    status=models.CharField(max_length=100,choices=status_choices ,verbose_name='وضعیت  ')
    localName=models.CharField(max_length=100,null=True,blank=True,verbose_name='محله ')
    description=models.CharField(max_length=100,null=True,blank=True,choices=description_choices,verbose_name=' علت عدم همکاری قبل از ورود')
    city=models.CharField(max_length=100,choices=city_choices,verbose_name='شهر ')
    description2=models.CharField(max_length=100,null=True,blank=True,choices=description_choices_2,verbose_name=' علت عدم همکاری بعد از ورود')
    description3=models.TextField(max_length=50,null=True,blank=True,verbose_name='یادداشت ')
    companyName=models.CharField(max_length=100,choices=company_name_choices,verbose_name='نوع شرکت ')
    canalAdvertising=models.CharField(max_length=100,verbose_name='کانال تبلیغاتی ')
    expertEdu=models.CharField(max_length=100,null=True,blank=True,choices=biker_edu_choices,verbose_name='کارشناس عملیات  ')
    bikerEdu=models.CharField(max_length=100,null=True,blank=True,verbose_name='سفیر آموزشی ')
    absrobResponse=models.CharField(max_length=100,null=True,blank=True,choices=absrob_response_choices,verbose_name='مسئول جذب ')
    createDate=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updateDate=models.DateField(auto_now=True,null=True,blank=True)
    confirmAbsrob= models.BooleanField(null=True,blank=True,verbose_name=' تایید فعال سازی اپ  ')
    absrobUser = models.ForeignKey("User", on_delete=models.CASCADE, null=True,verbose_name='کارشناس جذب  ')
    creditcard=models.BigIntegerField(null=True,blank=True,verbose_name=' شماره  کارت  ')
    creditcard2=models.BigIntegerField(null=True,blank=True,verbose_name=' شماره  حساب  ')
    creditcard3=models.BigIntegerField(null=True,blank=True,verbose_name=' شماره  شبا  ')
    vehicleAttach1=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='ضمیمه کارت  وسیله نقلیه')
    vehicleAttach2=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='ضمیمه بیمه نامه')
    vehicleAttach3=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='ضمیمه گواهی نامه')
    nationalAttach1=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='ضمیمه شناسنامه ص1')
    nationalAttach2=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='ضمیمه شناسنامه ص2')
    nationalAttach3=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='ضمیمه شناسنامه ص3')
    nationalAttach4=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='ضمیمه شناسنامه ص4')
    nationalAttach5=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='ضمیمه شناسنامه ص1-همسر')
    nationalAttach6=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='ضمیمه شناسنامه ص2-همسر')
    nationalAttach7=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='ضمیمه شناسنامه ص3-همسر')
    nationalAttach8=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='ضمیمه شناسنامه ص4-همسر')
    nationalAttach9=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='1ضمیمه شناسنامه ص1-فرزند')
    nationalAttach10=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='1ضمیمه شناسنامه ص2-فرزند')
    nationalAttach11=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='1ضمیمه شناسنامه ص3-فرزند')
    nationalAttach12=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='1ضمیمه شناسنامه ص4-فرزند')
    nationalAttach13=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='2ضمیمه شناسنامه ص1-فرزند')
    nationalAttach14=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='2ضمیمه شناسنامه ص2-فرزند')
    nationalAttach15=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='2ضمیمه شناسنامه ص3-فرزند')
    nationalAttach16=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name='2ضمیمه شناسنامه ص4-فرزند')
    leavingWorkAttach=models.ImageField(upload_to='home/%Y/%m/%d',null=True,blank=True,verbose_name=' فرم تسویه ')
    address=models.CharField(max_length=100,null=True,blank=True,verbose_name='آدرس ')
    date= jDateField( null=True,blank=True,verbose_name='تاریخ آماده به کار ')
    leavingWork=jDateField( null=True,blank=True,verbose_name='تاریخ ترک کار ')
    zoneName=models.CharField(max_length=250,null=True,blank=True,verbose_name=' نام زون  ')
    

    def __str__(self):
            return '%s %s' % (self.name,self.family,self.nationalCode )


class Comment_OP1(models.Model):
    Activate_app_model=models.ForeignKey(OP1,verbose_name="کد",on_delete=models.CASCADE,related_name='comments')
    Comment_follow=models.CharField(max_length=100,null=True,blank=True,verbose_name=" پیگیری "   )
    created_follow=models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return '%s %s' % (self.Activate_app_model, self.created_follow)
        
    def num_Comment_OP1(self):
        num_Comment_OP1 = Comment_OP1.objects.filter(uploaded_by=self).count()
        return num_Comment_OP1    
  
class User(AbstractBaseUser):
    
    email=models.EmailField(max_length=255,unique=True)
    phone_number=models.CharField(max_length=11,unique=True)
    full_name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True )
    is_admin=models.BooleanField(default=False )
    isAbsrob = models.BooleanField(("isAbsrob "),default=False)
    isPrimaryAbsrob = models.BooleanField(("isPrimaryAbsrob "),default=False)
    isInspection = models.BooleanField(("isInspection "),default=False)
    isAbsrobRegional = models.BooleanField(("isAbsrobRegional "),default=False)
    isExpertRegional = models.BooleanField(("isExpertRegional"),default=False)
    isManagerRegional = models.BooleanField(("isManagerRegional"),default=False)
    
    
    objects=UserManager()
     
 
    USERNAME_FIELD = 'phone_number'
     
    REQUIRED_FIELDS = ['email','full_name']
    
    def __str__(self):
        return self.email
    
    
    def has_perm(self, perm, obj=None):
        return True
        
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
   

class LogOp1(models.Model):
    
    op1 = models.ForeignKey(OP1, on_delete=models.CASCADE,related_name='logOp1')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=100, choices=[
        ("create", 'create'),
        ("delete", 'delete'),
        ("update", 'update'),
    ])
    created_at = models.DateTimeField(blank=True,null=True)
    change_name = models.CharField(max_length=200, null=True, blank=True)
    change_family = models.CharField(max_length=200, null=True, blank=True)
    change_national_code = models.BigIntegerField(null=True, blank=True)
    
    @property
    def last_update(self):
        pass