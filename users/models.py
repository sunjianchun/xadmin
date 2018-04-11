# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class Group(models.Model):
	name = models.CharField(max_length=60, null=False, verbose_name=u'组名')
	remark = models.CharField(max_length=60, null=True,verbose_name=u'备注')

	def __unicode__(self):
		return self.name

class UserInfo(models.Model):
	username = models.CharField(max_length=60, null=False, verbose_name=u'姓名')
	password = models.CharField(max_length=60, null=False, verbose_name=u'密码')
	count = models.IntegerField(default=0)
	date = models.DateTimeField(auto_now_add=True, null=True, blank=False)
	group = models.ForeignKey(Group)
	remark = models.CharField(max_length=60, null=True,verbose_name=u'备注')

	def __unicode__(self):
		return self.username



	
