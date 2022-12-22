"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Hasti_Parcel.views import user_login,regionalAbsrobDocDetail,absrob_detail_status,inspectionDetail,inspection,regionalAbsrobDoc,AbsrobDetail,regionalAbsrob,regionalEdu,regionalEduDetail,regionalAbsrobDetail,primaryAbsrob,primaryAbsrobDetail,Absrob,user_logout,importcsv,mainAbsrob,changepassword,forgetpassword,panel,reportData,reportDetail,absrob_detail_status
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',user_login),
    path('logout/',user_logout),
    path('changepassword/',changepassword),
    path('forgetpassword/',forgetpassword),
    path('',panel),


    path('mainAbsrob/', mainAbsrob ),
    path('importcsv/', importcsv ),
    
    path('Absrob/', Absrob ),
    
    path('AbsrobDetail/<int:id>/', AbsrobDetail ),
    path('absrob-detail-status/<int:id>/', absrob_detail_status , name="absrob-detail-status"),
        
    path('primaryAbsrob/', primaryAbsrob ),
    
    path('primaryAbsrobDetail/<int:id>/', primaryAbsrobDetail ),
  
    path('regionalAbsrob/', regionalAbsrob ),
    path('regionalAbsrobDetail/<int:id>/', regionalAbsrobDetail ),

    path('regionalEdu/', regionalEdu ),
    path('regionalEduDetail/<int:id>/', regionalEduDetail ),
    path('regionalAbsrobDoc/', regionalAbsrobDoc ),
  
    path('regionalAbsrobDocDetail/<int:id>/', regionalAbsrobDocDetail ),

    path('reportData/', reportData ),
    path('reportDetail/', reportDetail ),
    path('inspection/', inspection ),
    path('inspectionDetail/<int:id>/', inspectionDetail ),




]


if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)