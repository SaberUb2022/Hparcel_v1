from django.shortcuts import render
from django.contrib import messages
from django import forms
# Create your views here.
from django.forms.widgets import DateInput
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import OP1,User,LogOp1
from django_filters import DateFilter,CharFilter
from django.forms import DateInput
from django.db.models import Count
from django.utils import timezone
from .models import Comment_OP1

from django_jalali.forms import jDateField
from django_jalali.admin.widgets import AdminjDateWidget

from .forms import LoginForm,ChangePasswordForm,AbsrobDetail2Form,inspectionDetailForm,regionalAbsrobDocDetailForm,forgetpasswordForm,regionalAbsrobDetailForm,regionalEduDetailForm,mainAbsrobForm,AbsrobDetailForm,UserCreationForm,regionalAbsrobDetailForm,primaryAbsrobDetailForm
import datetime
from .filters import reportFilter

import django_filters 
from django.http import  HttpResponse
from django.forms.widgets import DateInput
from django.contrib.postgres.search import SearchVector
from email import message
from email.quoprimime import quote
from turtle import pd
import csv , io ,xlwt,jdatetime,datetime
from django_filters import DateFilter
from django.db.models import F


class primaryAbsrobFilter(django_filters.FilterSet):
     
     class Meta:
          model = OP1
          fields = ['branch','nationalCode','contractType','createDate','absrobResponse','date','expertEdu','city','phone_number']
     # date=jDateField(widget=AdminjDateWidget())     


class regionalAbsrobFilter(django_filters.FilterSet):
     class Meta:
          model = OP1
          fields = ['branch','nationalCode','contractType','createDate','absrobResponse','date','expertEdu','city','phone_number']
     date=jDateField(widget=AdminjDateWidget())     


class regionalEduFilter(django_filters.FilterSet):
     class Meta:
          model = OP1
          fields = ['branch','nationalCode','contractType','createDate','absrobResponse','date','expertEdu','city','phone_number']
     date=jDateField(widget=AdminjDateWidget())     


class absrobFilter(django_filters.FilterSet):
     class Meta:
          model = OP1
          fields = ['branch','nationalCode','contractType','createDate','absrobResponse','date','expertEdu','city','absrobUser','phone_number','status']
          


class report_data_Op1_Filter(django_filters.FilterSet):

    class Meta:
        model=OP1
        fields = ['branch','city','companyName','description','description2','contractType','vehicle','status']


def panel(request):
      
      context = {}
      return render(request,'Hasti_Parcel/panel.html', context)



def user_login(request):
     if request.method=='POST':
          form=LoginForm(request.POST)

          if form.is_valid():
               cd=form.cleaned_data
               user=authenticate(request,username=cd['username'],password=cd['password'])

               if user is not None:
                    if user.is_active:
                         login(request, user)
                         return redirect('/')
                    else:

                         return HttpResponse("اکانت شما غیر فعال است")

               else:
                    return HttpResponse(" اطلاعات شما نادرست است  ")
                    
     else:
          form=LoginForm()

     return render(request,'Hasti_Parcel/login.html',{'form':form})



def user_logout(request):
     user_logout(request)
     return redirect('/login/')



@login_required(login_url="/changepassword/")
def changepassword(request):
     
     if request.method=='POST':
          user=request.user

          form=ChangePasswordForm(request.POST)

          if form.is_valid():
               cd=form.cleaned_data
               old_password=cd["old_password"]
               new_password1=cd["new_password1"]
               new_password2=cd["new_password2"]

               #print("old_password",old_password)
               #print("new_password1",new_password1)
               #print("new_password2",new_password2)
               #print("user.password",user.password)

               if not user.check_password(old_password):
                    return HttpResponse("پسورد فعلی شما نادرست است")

               elif new_password1 != new_password2:
                    return HttpResponse("پسورد های جدید شما با هم مطابقت ندارند")
               else: 
                    user.set_password(new_password1)
                    user.save()
                    return HttpResponse("پسورد شما تغیر یافت  ")
                    
     else:
          form=ChangePasswordForm()

     return render(request,'Hasti_Parcel/ChangePasswordForm.html',{'form':form})

     


def forgetpassword(request):
     
     if request.method=='POST':
          user=request.user

          form=forgetpasswordForm(request.POST)

          if form.is_valid():
               cd=form.cleaned_data
               
               username=cd["username"]
               new_password1=cd["new_password1"]


               #print("old_password",old_password)
               #print("new_password1",new_password1)
               #print("new_password2",new_password2)
               #print("user.password",user.password)

               if not user.check_password(username):
                    return HttpResponse("پسورد فعلی شما نادرست است")
               else: 
                    user.set_password(new_password1)
                    user.save()
                    return HttpResponse("پسورد شما تغیر یافت  ")
                    
     else:
          form=ChangePasswordForm()

     return render(request,'Hasti_Parcel/forgetpassword.html',{'form':form})





def importcsv(request):
    
    prompt={
        'order' : 'order of the upload csv should be name,family,nationalCode,phone_number'
    }

    if request.method == 'GET':
       return render(request,'Hasti_Parcel/importcsv.html',prompt)


    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):

        message.error(request,'this is not csv file')
    else:
          
        

          data_set = csv_file.read().decode('UTF-8')
          io_string = io.StringIO(data_set)
          next(io_string)
          
          
          for column in csv.reader(io_string, delimiter=',', quotechar="|"):
               try:
                    int(column[2])
                    int(column[3])
               except:
                    messages.info(request, "شماره موبایل و کد ملی باید از جنس عدد باشد. خطا در وارد کردن اطلاعات ")
                    context= {}
                    return render(request,'Hasti_Parcel/import_Op1_csv.html',context)
               messages.add_message(request, messages.INFO, "اطلاعات با موفقیت ثبت شد")  
    
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
          try:
              user = User.objects.get(email=column[4])
          except:
               messages.add_message(request, messages.ERROR, " ایمیل غلط می باشد")  
               continue
         
          _ = OP1.objects.update_or_create(
               name=column[0],
               family=column[1],
               nationalCode=column[2],
               phone_number=column[3],
               absrobUser=user,
          )
         
    context = {}
    return render(request,'Hasti_Parcel/importcsv.html',context)    
    

 
 
def reportData(request):

     filter = report_data_Op1_Filter(request.GET, queryset=OP1.objects.all())
     context = {'filter': filter}
     return render(request,'Hasti_Parcel/reportData.html', context)

  

def reportDetail(request):
     response=HttpResponse(content_type='application/ms-excel')
     response['content-Disposition']='attachment;filename='+str(datetime.datetime.now())+'.xls'
     workbook=xlwt.Workbook(encoding='utf-8')
     worksheet=workbook.add_sheet('op_1')
     colunms=['name','family','nationalCode','phone_number',
                                   'branch','age','contractType','vehicle',
                                   'localName','description','city',
                                   'description2','companyName','canalAdvertising','expertEdu','createDate','updateDate','bikerEdu','description3']
     rownumber=0
     fontstyle=xlwt.XFStyle()
     for col in range(len(colunms)):
          worksheet.write(rownumber,col,colunms[col],fontstyle)

     filter = reportFilter(request.GET, queryset=OP1.objects.all())
     new_with_logs = filter.qs.annotate(op1_id=F('logOp1__op1_id'),action=F('logOp1__action'),id_log=F('logOp1__id')).values()
     # op_1=filter.qs.values_list('id','name','family','nationalCode','phone_number',
     #                               'branch','age','contractType','vehicle',
     #                               'localName','description','city',
     #                               'description2','companyName','canalAdvertising','expertEdu','createDate','updateDate','bikerEdu','description3')
     op_1=new_with_logs.values_list('id','name','family','nationalCode','phone_number',
                                   'branch','age','contractType','vehicle',
                                   'localName','description','city',
                                   'description2','companyName','canalAdvertising','expertEdu','createDate','updateDate','bikerEdu','description3','op1_id','action')

     for std in op_1:
          rownumber += 1    
          for col in range(len(std)):
               if isinstance(std[col], datetime.datetime):
                    dt2 : datetime.datetime = std[col]
                    jdt2 = jdatetime.datetime.fromgregorian(datetime=dt2)
                    
                    if colunms[col] == "createDate":
                         worksheet.write(rownumber,col,dt2.strftime("%m/%d/%Y %H:%M:%S"))
                    else:
                         worksheet.write(rownumber,col,jdt2.strftime("%a, %d %b %Y %H:%M:%S"))
               else:
                    worksheet.write(rownumber,col,std[col])
 
     workbook.save(response)
     return response

def mainAbsrob(request):
     if request.method== 'POST' :

          form=mainAbsrobForm(request.POST,request.FILES)
          if form.is_valid():
               op1 = OP1.objects.create(**form.cleaned_data)
               LogOp1.objects.create(op1=op1, user=request.user,action="create")
               messages.success(request,'اطلاعات با موفقیت ثبت شد')
               return redirect('/mainAbsrob/')
          else:
             messages.error(request,' شماره موبایل یا کدملی اشتباه می باشد ')  
               
     else:
          form = mainAbsrobForm()
     return  render(request,'Hasti_Parcel/mainAbsrob.html',{'form':form})

def Absrob(request):
     if request.user.isAbsrob or request.user.isAbsrobRegional or request.isPrimaryAbsrob or request.user.isManagerRegional:
          hom=OP1.objects.all().annotate(comment_count=Count("comments")).order_by("comment_count") 
          filter = absrobFilter(request.GET, queryset=hom)

          return render(request,'Hasti_Parcel/Absrob.html', {'hom': filter })
     return HttpResponse("شما دسترسی ندارید")


def AbsrobDetail(request,id):
     if request.user.isAbsrob or request.user.isAbsrobRegional or request.isPrimaryAbsrob or request.user.isManagerRegional:     
          
          Activate_app_model=OP1.objects.get(id=id)
     
          if request.method=='POST':
               form3=AbsrobDetailForm(request.POST,request.FILES)
               if form3.is_valid():
                    
                    obj=form3.save(commit=False)
                    obj.Activate_app_model=Activate_app_model
                    obj.save()
                    LogOp1.objects.create(op1=Activate_app_model, user=request.user,action="update")
                    return redirect(request.META['HTTP_REFERER'])    
          else: 
               form3=AbsrobDetailForm()
               form4=AbsrobDetail2Form() 
          context = {'Activate_app_model':Activate_app_model,'form3':form3,'form4':form4}
          return render(request,'Hasti_Parcel/AbsrobDetail.html', context)           
     return HttpResponse("شما دسترسی ندارید")


def absrob_detail_status(request, id):
     if request.user.isAbsrob or request.user.isAbsrobRegional or request.isPrimaryAbsrob or request.user.isManagerRegional:
          if request.method=='POST':
               op1 = OP1.objects.get(id=id)
               form=AbsrobDetail2Form(request.POST,request.FILES, instance=op1)
               if form.is_valid():
                    form.save()
     return redirect('/Absrob/',id=OP1.id)



def primaryAbsrob(request):
     if request.user.isPrimaryAbsrob or request.user.isManagerRegional:     
          hom=OP1.objects.all()
          filter = primaryAbsrobFilter(request.GET, queryset=hom)
          return render(request,'Hasti_Parcel/primaryAbsrob.html', {'hom': filter })
     return HttpResponse("شما دسترسی ندارید")


def primaryAbsrobDetail(request,id):
     if request.user.isPrimaryAbsrob or request.user.isManagerRegional:        
          
     
      
          # 'queryset' is wrong -> 'obj' is better
          queryset=OP1.objects.get(id=id)
          form=primaryAbsrobDetailForm(instance=queryset)
          if  request.method== 'POST' :
               form=primaryAbsrobDetailForm(request.POST,request.FILES,instance=queryset)
               if form.is_valid():
                    if 'name' in form.changed_data:
                         name = form.cleaned_data["name"]
                    else:
                         name= None
                    LogOp1.objects.create(op1=queryset, user=request.user, action="update", change_name=name)
                    LogOp1.objects.create(op1=queryset, user=request.user, action="update", created_at=timezone.now())
                    return redirect('/primaryAbsrob/')
          context = {'form':form}
          return render(request,'Hasti_Parcel/primaryAbsrobDetail.html', context)
     return HttpResponse("شما دسترسی ندارید")

def regionalAbsrob(request):
     if request.user.isAbsrobRegional or request.user.isManagerRegional:       
          hom=OP1.objects.all()
          filter = regionalAbsrobFilter(request.GET, queryset=hom)
          return render(request,'Hasti_Parcel/regionalAbsrob.html', {'hom': filter })
     return HttpResponse("شما دسترسی ندارید")

def regionalAbsrobDetail(request,id):
     if request.user.isAbsrobRegional or request.user.isManagerRegional:       
          queryset=OP1.objects.get(id=id)
          form=regionalAbsrobDetailForm(instance=queryset)
          if  request.method== 'POST' :
               form=regionalAbsrobDetailForm(request.POST,request.FILES,instance=queryset)
               if form.is_valid():
                    form.save()
                    return redirect('/regionalAbsrob/')
          context = {'form':form}
          return render(request,'Hasti_Parcel/regionalAbsrobDetail.html', context)
     return HttpResponse("شما دسترسی ندارید")


def regionalAbsrobDoc(request):
     if request.user.isAbsrobRegional or request.user.isManagerRegional:       
          hom=OP1.objects.all()
          filter = regionalAbsrobFilter(request.GET, queryset=hom)
          return render(request,'Hasti_Parcel/regionalAbsrobDoc.html', {'hom': filter })
     return HttpResponse("شما دسترسی ندارید")

     
def regionalAbsrobDocDetail(request,id):
     if request.user.isAbsrobRegional or request.user.isManagerRegional:       
          queryset=OP1.objects.get(id=id)
          form=regionalAbsrobDocDetailForm(instance=queryset)
          if  request.method== 'POST' :
               form=regionalAbsrobDocDetailForm(request.POST,request.FILES,instance=queryset)
               if form.is_valid():
                    form.save()
                    return redirect('/regionalAbsrobDoc/')
          context = {'form':form}
          return render(request,'Hasti_Parcel/regionalAbsrobDocDetail.html', context)
     return HttpResponse("شما دسترسی ندارید")


def regionalEdu(request):
     if request.user.isExpertRegional or request.user.isManagerRegional:       
          hom=OP1.objects.all()
          filter = regionalEduFilter(request.GET, queryset=hom)
          return render(request,'Hasti_Parcel/regionalEdu.html', {'hom': filter })
     return HttpResponse("شما دسترسی ندارید")


def regionalEduDetail(request,id):
     if request.user.isExpertRegional or request.user.isManagerRegional:       
          queryset=OP1.objects.get(id=id)
          form=regionalEduDetailForm(instance=queryset)
          if  request.method== 'POST' :
               form=regionalEduDetailForm(request.POST,instance=queryset)
               if form.is_valid():
                    form.save()
                    return redirect('/regionalEdu/')
          context = {'form':form}
          return render(request,'Hasti_Parcel/regionalEduDetail.html', context)
     return HttpResponse("شما دسترسی ندارید")



def inspection(request):
     if request.user.isInspection:       
          hom=OP1.objects.all()
          filter = regionalEduFilter(request.GET, queryset=hom)
          return render(request,'Hasti_Parcel/inspection.html', {'hom': filter })
     return HttpResponse("شما دسترسی ندارید")


def inspectionDetail(request,id):
     if request.user.isInspection :       
          queryset=OP1.objects.get(id=id)
          form=inspectionDetailForm(instance=queryset)
          if  request.method== 'POST' :
               form=inspectionDetailForm(request.POST,instance=queryset)
               if form.is_valid():
                    form.save()
                    return redirect('/inspection/')
          context = {'form':form}
          return render(request,'Hasti_Parcel/inspectionDetail.html', context)
     return HttpResponse("شما دسترسی ندارید")
