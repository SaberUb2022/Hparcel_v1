
from django import forms
from .models import OP1,Comment_OP1,User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django_jalali.forms import jDateField
from django_jalali.admin.widgets import AdminjDateWidget
import re
from django.forms import ModelForm, CharField, ValidationError


        
def phone_number_validator(value):
    """
    Validator For Phone Number
    Valid phone number = 09123456789
    """
    mobile_pattern = re.compile(r'^09[0-9]{9}$')

    if not mobile_pattern.match(value):
        raise ValidationError("شماره موبایل معتبر نیست")
    
    
    

def phone_number_validator2(value):
    if  len(value) == 0     :
        return value
    elif value.startswith("09") and len(value) == 11  :
        return value
    else:
        if value.startswith("9") and len(value) == 10  :
            return value   
    raise ValidationError("کاراکتر های شماره موبایل  یا کد ملی اشتباه است .")   
      
import math


def nationalCodeVaildation(value):
    if  str(value)=='':
        return value
    else:
        try:
            value = str(int(value))
        except ValueError:
            raise ValidationError("کاراکتر های کد ملی باید عددی باشد.")
        
        else:
            if len(value) ==10:
                return value  
    
    raise ValidationError("تعداد کارکترهای کد ملی اشتباه است .")   


class nationalcodeField(CharField):
      
    def validate(self, value):
        nationalCodeVaildation(value)
              

def normalize_phone_number(value):
    """Normalize Phone Number, Normal: 09*********"""
    try:
        value = str(int(value))
    except ValueError:
        raise ValidationError("کاراکتر های شماره موبایل باید عددی باشد.")

    if value.startswith("09"):
        return value
    if value.startswith("989"):
        return '0' + value[2:]
    if value.startswith("+989"):
        return '0' + value[3:]
    if value.startswith("9"):
        return '0' + value
    return value
  

class PhoneNumberField(CharField):
    def to_python(self, value):
        """Normalize data to a list of strings."""
        return normalize_phone_number(value)
    
    def validate(self, value):
        phone_number_validator(value)
        

class PhoneNumber2Field(CharField):
  
    def validate(self, value):
        phone_number_validator2(value)




class LoginForm(forms.Form):

    username=forms.CharField()
    password=forms.CharField()


class ChangePasswordForm(forms.Form):

    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())



def clean_new_password1(self):
    password = self.cleaned_data["new_password1"]
    if len(password) < 8  :
        raise forms.ValidationError("پسورد نباید کمتر از 8 کارکتر باشد")




class forgetpasswordForm(forms.Form):

    username = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput())


     

class AbsrobDetailForm(forms.ModelForm):
    
    class Meta:
        model =  Comment_OP1
        
        fields = ['Comment_follow']
       

 

class AbsrobDetail2Form(forms.ModelForm):
    
    class Meta:
        model =  Cmodel = OP1
        
        fields = ['status']
        
class mainAbsrobForm(forms.ModelForm):
    phone_number = PhoneNumberField(label="شماره موبایل کارکردی 1")
    nationalCode=nationalcodeField(required=False,label='کد ملی')
    class Meta:
        model = OP1
        fields = ['name','family','nationalCode','phone_number','city','canalAdvertising','companyName','status',"description",'description3']
    
      
class primaryAbsrobDetailForm(forms.ModelForm):
    class Meta:
            model = OP1
            fields = ['name','family','nationalCode','phone_number','city','canalAdvertising','companyName','age','vehicle','absrobResponse','date','leavingWork','leavingWorkAttach']
        
    date=jDateField(required=False, widget=AdminjDateWidget(),label='    تاریخ آماده به کار ')
    leavingWork=jDateField(required=False, widget=AdminjDateWidget(),label='    تاریخ ترک کار ')
        

class regionalAbsrobDetailForm(forms.ModelForm):
    class Meta:
        model = OP1
    def __init__(self,*args,**kwargs):
        super(regionalAbsrobDetailForm,self).__init__(*args, **kwargs)
        self.fields['name'].disabled=True
        self.fields['family'].disabled=True
        self.fields['nationalCode'].disabled=True
        self.fields['phone_number'].disabled=True
        self.fields['city'].disabled=True
        self.fields['age'].disabled=True
        self.fields['status'].disabled=True
        self.fields['description'].disabled=True
        self.fields['companyName'].disabled=True
        self.fields['canalAdvertising'].disabled=True
    class Meta:
        model = OP1
        fields = ['name','family','nationalCode','phone_number','branch','contractType','city','status','companyName','localName','canalAdvertising','vehicle','age','description','description2','expertEdu','description2','nationalCodeAttach']
      

class regionalEduDetailForm(forms.ModelForm):   
    def __init__(self,*args,**kwargs):
        super(regionalEduDetailForm,self).__init__(*args, **kwargs)
        self.fields['name'].disabled=True
        self.fields['family'].disabled=True
        self.fields['nationalCode'].disabled=True
        self.fields['phone_number'].disabled=True
        self.fields['city'].disabled=True
        self.fields['branch'].disabled=True
        self.fields['contractType'].disabled=True
        self.fields['age'].disabled=True
        self.fields['vehicle'].disabled=True
        self.fields['description2'].disabled=True
        self.fields['description'].disabled=True
        self.fields['expertEdu'].disabled=True
        self.fields['status'].disabled=True
        self.fields['description'].disabled=True
        self.fields['companyName'].disabled=True
        self.fields['canalAdvertising'].disabled=True       
    class Meta:
        model = OP1
        fields = ['name','family','nationalCode','phone_number','branch','contractType','city','status','companyName','localName','canalAdvertising','vehicle','age','description','expertEdu','description2','bikerEdu','zoneName']
       

class regionalAbsrobDocDetailForm(forms.ModelForm):
    phone_number2 = PhoneNumber2Field(required=False,label="شماره موبایل کارکردی 2") 
    def __init__(self,*args,**kwargs):
        super(regionalAbsrobDocDetailForm,self).__init__(*args, **kwargs)
        self.fields['name'].disabled=True
        self.fields['family'].disabled=True
        self.fields['nationalCode'].disabled=True
        self.fields['phone_number'].disabled=True
        self.fields['city'].disabled=True
        self.fields['branch'].disabled=True
        self.fields['contractType'].disabled=True 
      
    class Meta:
            model = OP1
            fields = ['name','family','nationalCode','phone_number','phone_number2','branch','city','status','companyName','localName','contractType','creditcard','creditcard2','creditcard3','vehicleAttach1','vehicleAttach2','vehicleAttach3','nationalAttach1','nationalAttach2','nationalAttach3','nationalAttach4','address','leavingWork']    
    
    leavingWork=jDateField(required=False,widget=AdminjDateWidget(),label='تاریخ ترک کار ')


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=('email','phone_number','full_name')
        
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] !=  cd['password2']:
            raise ValidationError('passwords not match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm) :   
    password  = ReadOnlyPasswordHashField(help_text="you can change password  using <a href=\"../password/\">this form </a>")
    class Meta:
        model = User
        fields=('email','phone_number','full_name','last_login')
         
    
class inspectionDetailForm(forms.ModelForm) : 

    def __init__(self,*args,**kwargs):
        super(inspectionDetailForm,self).__init__(*args, **kwargs)
        self.fields['name'].disabled=True
        self.fields['family'].disabled=True
        self.fields['companyName'].disabled=True
        self.fields['phone_number'].disabled=True
        self.fields['phone_number2'].disabled=True
        self.fields['city'].disabled=True
        self.fields['branch'].disabled=True
        self.fields['companyName'].disabled=True
        self.fields['vehicle'].disabled=True
      
    class Meta:
            model = OP1
            
            fields = ['name','family','nationalCode','phone_number','phone_number2','branch','city','companyName','vehicle','confirmAbsrob']  
       
    confirmAbsrob=forms.BooleanField( widget=forms.CheckboxInput)
           