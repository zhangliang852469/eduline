# -*- coding: utf-8 -*-
from django.db import models

from datetime import datetime


# Create your models here.

# 课程信息
class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=200, verbose_name='课程描述')
    detail = models.TextField(max_length=500, verbose_name='课程详情')
    is_banner = models.BooleanField(default=False, verbose_name='是否轮播')
    degree = models.CharField(max_length=2,
                              choices=(('cj', '初级'), ('zj', '中级'),
                                       ('gj', '高级')),
                              verbose_name='难度等级')
    learn_time = models.IntegerField(default=0, verbose_name='学习时长/分钟')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%M', verbose_name='封面', max_length=100)

    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    category = models.CharField(default='后端开发', verbose_name='课程类别', max_length=20)
    tag = models.CharField(max_length=10, default='', verbose_name='课程标签')
    youneeded_know = models.CharField(max_length=300, default='', verbose_name='课程须知')
    teacher_tell = models.CharField(max_length=300, default='', verbose_name='老师告诉你')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 章节信息
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名称')
    daa_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 视频信息
class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名称')
    url = models.URLField(max_length=200, verbose_name='访问地址', default='')
    learn_time = models.IntegerField(default=0, verbose_name='学习时长')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 课程资料信息
class CourseResource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='名称')
    download = models.FileField(upload_to='course/resource/%Y/%M', verbose_name='资源下载')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<<{0}>>课程的课程资料》{1}'.format(self.course, self.name)






