# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-06-11 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app01', '0007_auto_20180611_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name_plural': '校区',
                'verbose_name': '校区',
            },
        ),
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_type', models.SmallIntegerField(choices=[(0, '面授'), (1, '随到随学网络')], default=0)),
                ('total_class_nums', models.PositiveIntegerField(default=10, verbose_name='课程总节次')),
                ('semester', models.IntegerField(verbose_name='学期')),
                ('price', models.IntegerField(default=10000, verbose_name='学费')),
                ('start_date', models.DateField(verbose_name='开班日期')),
                ('graduate_date', models.DateField(blank=True, null=True, verbose_name='结业日期')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Branch', verbose_name='校区')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='课程名')),
                ('description', models.TextField(verbose_name='课程描述')),
                ('outline', models.TextField(verbose_name='课程大纲')),
                ('period', models.IntegerField(verbose_name='课程周期(Month)')),
            ],
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_num', models.IntegerField(help_text='此处填写第几节课或第几天课程...,必须为数字', verbose_name='节次')),
                ('date', models.DateField(auto_now_add=True, verbose_name='上课日期')),
                ('has_homework', models.BooleanField(default=True, verbose_name='本节有作业')),
                ('homework_title', models.CharField(blank=True, max_length=128, null=True)),
                ('homework_requirement', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList', verbose_name='班级(课程)')),
            ],
            options={
                'verbose_name_plural': '上课纪录',
                'verbose_name': '上课纪录',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qq', models.CharField(help_text='QQ号必须唯一', max_length=64, unique=True)),
                ('qq_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='QQ名称')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=32, verbose_name='性别')),
                ('birthday', models.DateField(blank=True, help_text='格式yyyy-mm-dd', max_length=64, null=True, verbose_name='出生日期')),
                ('phone', models.BigIntegerField(blank=True, null=True, verbose_name='手机号')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='常用邮箱')),
                ('id_num', models.CharField(blank=True, max_length=64, null=True, verbose_name='身份证号')),
                ('source', models.CharField(choices=[('qq', 'qq群'), ('referral', '内部转介绍'), ('website', '官方网站'), ('baidu_ads', '百度广告'), ('qq_class', '腾讯课堂'), ('school_propaganda', '高校宣讲'), ('51cto', '51cto'), ('others', '其它')], default='qq', max_length=64, verbose_name='客户来源')),
                ('class_type', models.CharField(choices=[('online', '网络班'), ('offline_weekend', '面授班(周末)'), ('offline_fulltime', '面授班(脱产)')], max_length=64, verbose_name='班级类型')),
                ('customer_note', models.TextField(help_text='客户咨询的大概情况,客户个人信息备注等...', verbose_name='客户咨询内容详情')),
                ('work_status', models.CharField(choices=[('employed', '在职'), ('unemployed', '无业')], default='employed', max_length=32, verbose_name='职业状态')),
                ('company', models.CharField(blank=True, max_length=64, null=True, verbose_name='目前就职公司')),
                ('salary', models.CharField(blank=True, max_length=64, null=True, verbose_name='当前薪资')),
                ('status', models.CharField(choices=[('signed', '已报名'), ('unregistered', '未报名')], default='unregistered', help_text='选择客户此时的状态', max_length=64, verbose_name='状态')),
                ('date', models.DateField(auto_now_add=True, verbose_name='咨询日期')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerFollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(verbose_name='跟进内容...')),
                ('status', models.IntegerField(choices=[(1, '近期无报名计划'), (2, '2个月内报名'), (3, '1个月内报名'), (4, '2周内报名'), (5, '1周内报名'), (6, '2天内报名'), (7, '已报名'), (8, '已交全款')], help_text='选择客户此时的状态', verbose_name='状态')),
                ('date', models.DateField(auto_now_add=True, verbose_name='跟进日期')),
            ],
            options={
                'verbose_name_plural': '客户咨询跟进记录',
                'verbose_name': '客户咨询跟进记录',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled_date', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='报名日期')),
                ('why_us', models.TextField(blank=True, default=None, max_length=1024, null=True, verbose_name='为什么报名老男孩')),
                ('your_expectation', models.TextField(blank=True, max_length=1024, null=True, verbose_name='学完想达到的具体期望')),
                ('contract_agreed', models.BooleanField(verbose_name='我已认真阅读完培训协议并同意全部协议内容')),
                ('contract_approved', models.BooleanField(help_text='在审阅完学员的资料无误后勾选此项,合同即生效', verbose_name='审批通过')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('course_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList', verbose_name='所报班级')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Branch', verbose_name='校区')),
            ],
            options={
                'verbose_name_plural': '学员报名表',
                'verbose_name': '学员报名表',
            },
        ),
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_type', models.CharField(choices=[('deposit', '订金/报名费'), ('tution', '学费'), ('refund', '退款')], default='deposit', max_length=64, verbose_name='费用类型')),
                ('paid_fee', models.IntegerField(default=0, verbose_name='费用数额')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='交款日期')),
            ],
            options={
                'verbose_name_plural': '交款纪录',
                'verbose_name': '交款纪录',
            },
        ),
        migrations.CreateModel(
            name='StuAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('valid_start', models.DateTimeField(blank=True, null=True, verbose_name='账户有效期开始')),
                ('valid_end', models.DateTimeField(blank=True, null=True, verbose_name='账户有效期截止')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.CharField(choices=[('checked', '已签到'), ('late', '迟到'), ('noshow', '缺勤'), ('leave_early', '早退')], default='checked', max_length=64, verbose_name='上课纪录')),
                ('score', models.IntegerField(choices=[(100, 'A+'), (90, 'A'), (85, 'B+'), (80, 'B'), (70, 'B-'), (60, 'C+'), (50, 'C'), (40, 'C-'), (-50, 'D'), (0, 'N/A'), (-100, 'COPY'), (-1000, 'FAIL')], default=-1, verbose_name='本节成绩')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
                ('course_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.CourseRecord', verbose_name='第几天课程')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='学员')),
            ],
            options={
                'verbose_name_plural': '学员学习纪录',
                'verbose_name': '学员学习纪录',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('memo', models.TextField(blank=True, default=None, null=True, verbose_name='备注')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Branch', verbose_name='所属校区')),
                ('roles', models.ManyToManyField(blank=True, to='app01.Role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='paymentrecord',
            name='consultant',
            field=models.ForeignKey(help_text='谁签的单就选谁', on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='负责老师'),
        ),
        migrations.AddField(
            model_name='paymentrecord',
            name='enrollment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Enrollment'),
        ),
        migrations.AddField(
            model_name='customerfollowup',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='跟踪人'),
        ),
        migrations.AddField(
            model_name='customerfollowup',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='所咨询客户'),
        ),
        migrations.AddField(
            model_name='customer',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='课程顾问'),
        ),
        migrations.AddField(
            model_name='customer',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='咨询课程'),
        ),
        migrations.AddField(
            model_name='customer',
            name='referral_from',
            field=models.ForeignKey(blank=True, help_text='若此客户是转介绍自内部学员,请在此处选择内部＼学员姓名', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='internal_referral', to='crm.Customer', verbose_name='转介绍自学员'),
        ),
        migrations.AddField(
            model_name='courserecord',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='讲师'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(to='crm.UserProfile', verbose_name='讲师'),
        ),
        migrations.AlterUniqueTogether(
            name='studyrecord',
            unique_together=set([('course_record', 'student')]),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('customer', 'course_grade')]),
        ),
        migrations.AlterUniqueTogether(
            name='courserecord',
            unique_together=set([('course', 'day_num')]),
        ),
    ]
