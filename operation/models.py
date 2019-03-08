# -*- coding: utf-8 -*-
from django.db import models

from datetime import datetime

from user.models import UserProfile

from courses.models import Course
# Create your models here.

# 用户的 我要学习信息
class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.ImageField(max_length=11, verbose_name='手机')
    course_name = models.CharField(max_length=50, verbose_name='课程名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 课程评论
class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户名')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    comment = models.CharField(max_length=200, verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment

# 用户收藏信息
class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    fav_id = models.IntegerField(default=0, verbose_name='数据ID')
    fav_type = models.CharField(max_length=20, choices=(('1', '课程'), ('2', '机构'), ('3', '讲师')), verbose_name='收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='收藏时间')

    class Meta:
        verbose_name = '用户收藏信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user

# 用户消息
class UserMessage(models.Model):
    # 我们的消息有两种:一种是发给全员，另一种则是发给特定某一个用户。
    # 所以如果使用外键，那么每个消息就要对应一个用户，比较难以实现全员消息的通知。
    # 因此我们设置用户id,如果为0就发给所有用户，不为0就是发给特定Id的用户。
    user = models.IntegerField(default=0, verbose_name='用户ID')
    message = models.CharField(max_length=500, verbose_name='消息内容')
    # 设置消息是否已读
    message_readed = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message

# 用户课程信息
class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='学习时间')

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user































