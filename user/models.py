# -*- coding: utf-8 -*-

from django.db import models

from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class UserProfile(AbstractBaseUser):
    name = models.CharField(max_length=50, verbose_name='昵称', default='')
    birday = models.DateTimeField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=6, verbose_name='性别', choices=(('male', '男'), ('female', '女')), default='male')
    address = models.CharField(max_length=200, default='', verbose_name='地址')
    mobile = models.CharField(max_length=100, verbose_name='手机号', null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%M', default='image/default.png', max_length=100, verbose_name='图片')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.get_username()


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=20, verbose_name='验证类型',
                                 choices=(('register', '注册'), ('forget', '找回'),
                                          ('update_email', '修改邮箱')))
    send_time = models.DateTimeField(verbose_name='发送时间', default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email

class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%M', verbose_name='轮播图')
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='轮播顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title















