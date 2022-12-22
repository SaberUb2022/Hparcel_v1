from django.contrib import admin

from .models import OP1,LogOp1
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from . forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import Group
# Register your models here.

admin.site.register(OP1)

class UserAdmin(BaseUserAdmin):
    
    form = UserChangeForm
    add_form =  UserCreationForm
    
    
    list_display =('email','phone_number','is_admin')
    list_filter = ('is_admin',)
    
    fieldsets = (
        (None,{'fields':('email','phone_number','full_name','password')}),
        ('permissions',{'fields':('is_active','is_admin','last_login','isAbsrob','isPrimaryAbsrob','isAbsrobRegional','isManagerRegional','isExpertRegional','isInspection')}),
        
    )
    
    add_fieldsets = (
        (None,{'fields':('phone_number','email','full_name','password1','password2')}),
        
    )
    
    search_fields = ('email','full_name')
    ordering = ('full_name',)
    filter_horizontal=()
    
    
admin.site.unregister(Group)
admin.site.register(User,UserAdmin)



class LogOp1Admin(admin.ModelAdmin):
    list_display = ("get_op1_name", "created_at", "action", "change_name",'user')
    fields = ("created_at", "user")
    date_hierarchy = "created_at"

    @admin.display(description='Name')
    def get_op1_name(self, obj):
        return obj.op1.name

admin.site.register(LogOp1, LogOp1Admin)