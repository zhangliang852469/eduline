# -*- coding: utf-8 -*-
from django.db import models

from datetime import datetime

# Create your models here.

# 城市信息
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市')
    desc = models.CharField(max_length=200, verbose_name='描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 课程机构
class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述')
    tag = models.CharField(max_length=10, verbose_name='机构标签', default='全国知名')
    category = models.CharField(max_length=50, default='pxjg', choices=(('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')), verbose_name='机构类别')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    image = models.ImageField(max_length=50, upload_to='organization/%Y/%M', verbose_name='logo')
    address = models.CharField(max_length=50, verbose_name='机构地址')

    city = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name='所在城市说明')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    course_nums = models.IntegerField(default=0, verbose_name='课程数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 教师信息
class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name='所属教师')
    name = models.CharField(max_length=50, verbose_name='教师名称')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    work_position = models.CharField(max_length=50, verbose_name='公司职位')
    work_company = models.CharField(max_length=50, verbose_name='就职公司')
    points = models.CharField(max_length=50, verbose_name='教学特点')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    age = models.IntegerField(default=18, verbose_name='年龄')
    image = models.ImageField(default='', upload_to='teacher/%Y/%M', verbose_name='头像', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name











