from django.db import models


# Create your models here.


class UserInfo(models.Model):
    userID = models.IntegerField(primary_key=True)
    realName = models.CharField(max_length=20)
    mobile = models.IntegerField(max_length=11)
    gender = models.BooleanField()
    marriage = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=256)
    qq = models.IntegerField()
    wechat = models.CharField(max_length=128)


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=64)
    salt = models.CharField(max_length=16)
    status = models.BooleanField()
    createTime = models.DateTimeField()
    updateTime = models.DateTimeField()
    lastLoginTime = models.DateTimeField()
    loginSuccessSumDay = models.IntegerField()


class AccessHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.ForeignKey(User)
    accessCode = models.CharField()
    accessURL = models.CharField(max_length=1024)
    accessType = models.CharField()
    accessIP = models.CharField()
    accessBrowser = models.CharField()
    accessDevice = models.CharField()
    loginTime = models.DateTimeField(auto_now=True)



