# Generated by Django 4.1.3 on 2022-12-18 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('isAbsrob', models.BooleanField(default=False, verbose_name='isAbsrob ')),
                ('isPrimaryAbsrob', models.BooleanField(default=False, verbose_name='isPrimaryAbsrob ')),
                ('isInspection', models.BooleanField(default=False, verbose_name='isInspection ')),
                ('isAbsrobRegional', models.BooleanField(default=False, verbose_name='isAbsrobRegional ')),
                ('isExpertRegional', models.BooleanField(default=False, verbose_name='isExpertRegional')),
                ('isManagerRegional', models.BooleanField(default=False, verbose_name='isManagerRegional')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OP1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام ')),
                ('family', models.CharField(max_length=100, verbose_name=' نام خانوادگی  ')),
                ('nationalCode', models.CharField(blank=True, max_length=100, null=True, verbose_name=' کد ملی  ')),
                ('nationalCodeAttach', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d')),
                ('phone_number', models.BigIntegerField(verbose_name=' شماره موبایل کارکرد1  ')),
                ('phone_number2', models.CharField(blank=True, max_length=100, null=True, verbose_name=' شماره موبایل کارکرد2  ')),
                ('branch', models.CharField(blank=True, choices=[('تهران جنوب شرق', 'تهران جنوب شرق'), ('تهران جنوب غرب', 'تهران جنوب غرب'), ('تهران شمال شرق', 'تهران شمال شرق'), ('تهران شمال غرب', 'تهران شمال غرب'), ('شعبه استان فارس', 'شعبه استان فارس'), ('شعبه استان اصفهان', 'شعبه استان اصفهان'), ('شعبه استان لرستان', 'شعبه استان لرستان'), ('شعبه استان کرمانشاه', 'شعبه استان کرمانشاه'), ('شعبه استان گيلان', 'شعبه استان گيلان'), ('شعبه کرمانشاه 2', 'شعبه کرمانشاه 2'), ('شعبه مازندران2', 'شعبه مازندران2'), ('شعبه استان سمنان', 'شعبه استان سمنان'), ('شعبه استان کرمان', 'شعبه استان کرمان'), (' استان البرز2', ' استان البرز2'), ('شعبه استان مازندران', 'شعبه استان مازندران'), ('شعبه استان همدان', 'شعبه استان همدان'), ('شعبه استان آذربايجان غربي', 'شعبه استان آذربايجان غربي'), ('شعبه آذربايجان شرقي2', 'شعبه آذربايجان شرقي2'), ('شعبه استان خوزستان', 'شعبه استان خوزستان'), ('شعبه استان خراسان رضوي', 'شعبه استان خراسان رضوي'), ('استان خوزستان 2', 'استان خوزستان 2'), ('شعبه استان قزوين', 'شعبه استان قزوين'), ('شعبه استان ايلام', 'شعبه استان ايلام'), ('شعبه استان خراسان شمالي', 'شعبه استان خراسان شمالي'), (' شعبه استان قم', ' شعبه استان قم'), ('شعبه استان البرز', 'شعبه استان البرز'), ('شعبه استان بوشهر', 'شعبه استان بوشهر'), ('شعبه استان کردستان', 'شعبه استان کردستان'), ('شعبه گيلان2', 'شعبه گيلان2'), ('شعبه استان هرمزگان', 'شعبه استان هرمزگان'), ('شعبه استان اردبيل', 'شعبه استان اردبيل'), ('شعبه استان آذربايجان شرقي', 'شعبه استان آذربايجان شرقي'), ('شعبه استان خراسان جنوبي', 'شعبه استان خراسان جنوبي'), ('شعبه يزد 2', 'شعبه يزد 2'), ('شعبه استان گلستان', 'شعبه استان گلستان'), ('شعبه استان چهارمحال و بختياري', 'شعبه استان چهارمحال و بختياري'), ('شعبه استان يزد', 'شعبه استان يزد'), ('شعبه استان مرکزي', 'شعبه استان مرکزي'), ('شعبه استان زنجان', 'شعبه استان زنجان'), ('شعبه استان کهکيلويه و بويراحمد', 'شعبه استان کهکيلويه و بويراحمد'), ('شعبه استان سيستان و بلوچستان', 'شعبه استان سيستان و بلوچستان')], max_length=100, null=True, verbose_name='شعبه ')),
                ('age', models.BigIntegerField(blank=True, null=True, verbose_name='سن ')),
                ('contractType', models.CharField(blank=True, choices=[('استخدامی', 'استخدامی'), ('پیمانی', 'پیمانی')], max_length=100, null=True, verbose_name='نوع قرارداد ')),
                ('vehicle', models.CharField(blank=True, choices=[('خودرو', 'خودرو'), ('موتورسیکلت', 'موتورسیکلت'), ('موتورسیکلت /خودرو', 'موتورسیکلت /خودرو'), ('وانت', 'وانت')], max_length=100, null=True, verbose_name='وسیله نقلیه ')),
                ('status', models.CharField(choices=[('منفی', 'منفی'), ('مثبت', 'مثبت'), ('بی پاسخ', 'بی پاسخ'), ('ورود به دفتر', 'ورود به دفتر')], max_length=100, verbose_name='وضعیت  ')),
                ('localName', models.CharField(blank=True, max_length=100, null=True, verbose_name='محله ')),
                ('description', models.CharField(blank=True, choices=[('اتباع ', 'اتباع '), ('درخواست بیمه -مدارک لازم ندارد', 'درخواست بیمه -مدارک لازم ندارد'), ('وسیله نقلیه مورد نظر را ندارد', 'وسیله نقلیه مورد نظر را ندارد'), ('انصراف(ساعت کاری)', 'انصراف(ساعت کاری)'), ('انصراف(درآمد کم)', 'انصراف(درآمد کم)'), ('کسری مدارک(امکان تکمیل ندارد)', 'کسری مدارک(امکان تکمیل ندارد)'), ('سن متقاضی بالای 50 یا زیر 16', 'سن متقاضی بالای 50 یا زیر 16'), ('ساکن شهر دیگر', 'ساکن شهر دیگر'), ('سایر', 'سایر')], max_length=100, null=True, verbose_name=' علت عدم همکاری قبل از ورود')),
                ('city', models.CharField(choices=[('تهران', 'تهران'), ('مشهد', 'مشهد'), ('اهواز', 'اهواز'), ('شيراز', 'شيراز'), ('اصفهان', 'اصفهان'), ('قم', 'قم'), ('قزوين', 'قزوين'), ('اسلامشهر', 'اسلامشهر'), ('کرج', 'کرج'), ('تبريز', 'تبريز'), ('همدان', 'همدان'), ('بيرجند', 'بيرجند'), ('کرمانشاه', 'کرمانشاه'), ('اردبيل', 'اردبيل'), ('اروميه', 'اروميه'), ('رشت', 'رشت'), ('گنبد كاووس', 'گنبد كاووس'), ('بابل', 'بابل'), ('گرگان', 'گرگان'), ('يزد', 'يزد'), ('اراک', 'اراک'), ('پرند', 'پرند'), ('خرم آباد', 'خرم آباد'), ('بجنورد', 'بجنورد'), ('زاهدان', 'زاهدان'), ('قرچک', 'قرچک'), ('مرند', 'مرند'), ('نيشابور', 'نيشابور'), ('زنجـان', 'زنجـان'), ('پرديس', 'پرديس'), ('ايلام', 'ايلام'), ('شاهرود', 'شاهرود'), ('سمنان', 'سمنان'), ('کاشمر', 'کاشمر'), ('نسيم شهر', 'نسيم شهر'), ('سنندج', 'سنندج'), ('ساري', 'ساري'), ('بروجرد', 'بروجرد'), ('سقز', 'سقز'), ('شهر قدس', 'شهر قدس'), ('پاکدشت', 'پاکدشت'), ('شوشتر', 'شوشتر'), ('گلبهار', 'گلبهار'), ('کاشان', 'کاشان'), ('گناوه', 'گناوه'), ('ساوه', 'ساوه'), ('مراغه', 'مراغه'), ('صدرا', 'صدرا'), ('شاهين شهر', 'شاهين شهر'), ('قائن', 'قائن'), ('بومهن', 'بومهن'), ('ملاير', 'ملاير'), ('ورامين', 'ورامين'), ('تربت حيدريه', 'تربت حيدريه'), ('دهدشت', 'دهدشت'), ('شيروان', 'شيروان'), ('نورآباد ممسني', 'نورآباد ممسني'), ('خوي', 'خوي'), ('بهارستان', 'بهارستان'), ('خرمشهر', 'خرمشهر'), ('کازرون', 'کازرون'), ('تربت جام', 'تربت جام'), ('ماهشهر', 'ماهشهر'), ('اندیشه', 'اندیشه'), ('مسجد سليمان', 'مسجد سليمان'), ('خواف', 'خواف'), ('لنگرود', 'لنگرود'), ('آبادان', 'آبادان'), ('کلاچاي', 'کلاچاي'), ('قوچان', 'قوچان'), ('ياسوج', 'ياسوج'), ('جهرم', 'جهرم'), ('مهاباد', 'مهاباد'), ('ايذه', 'ايذه'), ('كوهدشت', 'كوهدشت'), ('برازجان', 'برازجان'), ('شوش', 'شوش'), ('شهر کرد', 'شهر کرد'), ('گچساران', 'گچساران'), ('لاهيجان', 'لاهيجان'), ('اسلام آباد غرب', 'اسلام آباد غرب'), ('درود', 'درود'), ('بوشهر', 'بوشهر'), ('ميانه', 'ميانه'), ('اهر', 'اهر'), ('انديمشك', 'انديمشك'), ('انزلي', 'انزلي'), ('رفسنجان', 'رفسنجان'), ('لار', 'لار'), ('بابلسر', 'بابلسر'), ('آمل', 'آمل'), ('اردبیل', 'اردبیل'), ('بوكان', 'بوكان'), ('سپاهان شهر', 'سپاهان شهر'), ('اسفراين', 'اسفراين'), ('پارس آباد', 'پارس آباد'), ('رودسر', 'رودسر'), ('انـزلـي', 'انـزلـي')], max_length=100, verbose_name='شهر ')),
                ('description2', models.CharField(blank=True, choices=[('اتباع ', 'اتباع '), ('درخواست بیمه -مدارک لازم ندارد', 'درخواست بیمه -مدارک لازم ندارد'), ('وسیله نقلیه مورد نظر را ندارد', 'وسیله نقلیه مورد نظر را ندارد'), ('انصراف(ساعت کاری)', 'انصراف(ساعت کاری)'), ('انصراف(درآمد کم)', 'انصراف(درآمد کم)'), ('کسری مدارک(امکان تکمیل ندارد)', 'کسری مدارک(امکان تکمیل ندارد)'), ('سن متقاضی بالای 50 یا زیر 16', 'سن متقاضی بالای 50 یا زیر 16'), (' در آینده مراجعه میکند(دلیل در توضیحات) ', ' در آینده مراجعه میکند(دلیل در توضیحات) '), (' عدم مراجعه ', ' عدم مراجعه '), ('کسری مدارک(به زودی تکمیل و مراجعه میکند)  ', 'کسری مدارک(به زودی تکمیل و مراجعه میکند)  '), ('مردود(ظاهر-رفتار-توانائی)  ', 'مردود(ظاهر-رفتار-توانائی)  '), ('ساکن شهر دیگر', 'ساکن شهر دیگر'), ('سایر', 'سایر')], max_length=100, null=True, verbose_name=' علت عدم همکاری بعد از ورود')),
                ('description3', models.TextField(blank=True, max_length=50, null=True, verbose_name='یادداشت ')),
                ('companyName', models.CharField(choices=[('اکالا', 'اکالا'), ('افق کوروش', 'افق کوروش')], max_length=100, verbose_name='نوع شرکت ')),
                ('canalAdvertising', models.CharField(max_length=100, verbose_name='کانال تبلیغاتی ')),
                ('expertEdu', models.CharField(blank=True, choices=[('کارشناس 1 ', ' کارشناس 1'), ('کارشناس 2 ', ' کارشناس 2'), ('کارشناس 3 ', ' کارشناس 3'), ('کارشناس 4 ', ' کارشناس 4'), ('کارشناس 5 ', ' کارشناس 5'), ('کارشناس 6 ', ' کارشناس 6'), ('کارشناس 7 ', ' کارشناس 7'), ('کارشناس 8 ', ' کارشناس 8')], max_length=100, null=True, verbose_name='کارشناس عملیات  ')),
                ('bikerEdu', models.CharField(blank=True, max_length=100, null=True, verbose_name='سفیر آموزشی ')),
                ('absrobResponse', models.CharField(blank=True, choices=[('مسئول جذب 1', 'مسئول جذب 1'), ('مسئول جذب 2', 'مسئول جذب 2'), ('مسئول جذب 3', 'مسئول جذب 3')], max_length=100, null=True, verbose_name='مسئول جذب ')),
                ('createDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('updateDate', models.DateField(auto_now=True, null=True)),
                ('confirmAbsrob', models.BooleanField(blank=True, null=True, verbose_name=' تایید فعال سازی اپ  ')),
                ('creditcard', models.BigIntegerField(blank=True, null=True, verbose_name=' شماره  کارت  ')),
                ('creditcard2', models.BigIntegerField(blank=True, null=True, verbose_name=' شماره  حساب  ')),
                ('creditcard3', models.BigIntegerField(blank=True, null=True, verbose_name=' شماره  شبا  ')),
                ('vehicleAttach1', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='ضمیمه کارت  وسیله نقلیه')),
                ('vehicleAttach2', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='ضمیمه بیمه نامه')),
                ('vehicleAttach3', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='ضمیمه گواهی نامه')),
                ('nationalAttach1', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='ضمیمه شناسنامه ص1')),
                ('nationalAttach2', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='ضمیمه شناسنامه ص2')),
                ('nationalAttach3', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='ضمیمه شناسنامه ص3')),
                ('nationalAttach4', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='ضمیمه شناسنامه ص4')),
                ('nationalAttach5', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='ضمیمه شناسنامه ص1-همسر')),
                ('nationalAttach6', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='ضمیمه شناسنامه ص2-همسر')),
                ('nationalAttach7', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='ضمیمه شناسنامه ص3-همسر')),
                ('nationalAttach8', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='ضمیمه شناسنامه ص4-همسر')),
                ('nationalAttach9', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='1ضمیمه شناسنامه ص1-فرزند')),
                ('nationalAttach10', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='1ضمیمه شناسنامه ص2-فرزند')),
                ('nationalAttach11', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='1ضمیمه شناسنامه ص3-فرزند')),
                ('nationalAttach12', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='1ضمیمه شناسنامه ص4-فرزند')),
                ('nationalAttach13', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='2ضمیمه شناسنامه ص1-فرزند')),
                ('nationalAttach14', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='2ضمیمه شناسنامه ص2-فرزند')),
                ('nationalAttach15', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='2ضمیمه شناسنامه ص3-فرزند')),
                ('nationalAttach16', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name='2ضمیمه شناسنامه ص4-فرزند')),
                ('leavingWorkAttach', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d', verbose_name=' فرم تسویه ')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='آدرس ')),
                ('date', django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='تاریخ آماده به کار ')),
                ('leavingWork', django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='تاریخ ترک کار ')),
                ('zoneName', models.CharField(blank=True, max_length=250, null=True, verbose_name=' نام زون  ')),
                ('absrobUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کارشناس جذب  ')),
            ],
        ),
        migrations.CreateModel(
            name='LogOp1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('create', 'create'), ('delete', 'delete'), ('update', 'update')], max_length=100)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('change_name', models.CharField(blank=True, max_length=200, null=True)),
                ('change_family', models.CharField(blank=True, max_length=200, null=True)),
                ('change_national_code', models.BigIntegerField(blank=True, null=True)),
                ('op1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logOp1', to='Hasti_Parcel.op1')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment_OP1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment_follow', models.CharField(blank=True, max_length=100, null=True, verbose_name=' پیگیری ')),
                ('created_follow', models.DateTimeField(auto_now_add=True)),
                ('Activate_app_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Hasti_Parcel.op1', verbose_name='کد')),
            ],
        ),
    ]