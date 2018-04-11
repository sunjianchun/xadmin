# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from .models import * 

import xadmin
from xadmin.plugins.actions import BaseActionView

class MyAction(BaseActionView):
	action_name = "modify"
	description = _(u'修改所选的%(verbose_name_plural)s')
	
	model_perm = 'change'
	
	def do_action(self, queryset):
		for obj in queryset:
			print obj.id
		
		return HttpResponse(u"可以了")


class UserInfoAdmin(object):
	actions = [MyAction, ]
	list_display = ("username", "remark", "date")
	list_filter = ("username",)
	fields = ("username", "password", "group", "count", "remark",)
	list_export = ('json',)
	refresh_times = (3, 5, 7,)
	show_detail_fields = ["group", "password",]
	list_editable = ['username', 'password', 'date', 'remark', ]

	data_charts = {
        "id_trace": {'title': u"User Report", "x-field": "date", "y-field": ("id"), "order": ('date',)},
        "count_trace": {'title': u"Avg Report", "x-field": "date", "y-field": ('count',), "order": ('date',)}
    	}

class GroupAdmin(object):
	actions = [MyAction, ]
	list_display = ("name", "remark")
	list_filter = ("name",)


xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(Group, GroupAdmin)
from xadmin.sites import site
from xadmin.views import BaseAdminView, CommAdminView

class MyAdminView(BaseAdminView):

	def get(self, request, *args, **kwargs):
		return HttpResponse("nice")

site.register_view(r'^me_test/$', MyAdminView, name='my_test')
class AdminSettings(object):
    site_title = u'工单系统'
    site_footer = u'孙建春的公司'

    def get_site_menu(self):
        return (
            {'title': '内容管理', 'perm': self.get_model_perm(UserInfo, 'change'), 'menus':(
                {'title': '游戏资料', 'icon': 'info-sign', 'url': self.get_model_url(UserInfo, 'changelist') + '?_rel_categories__id__exact=2'},
                {'title': '网站文章', 'icon': 'file', 'url': self.get_model_url(UserInfo, 'changelist') + '?_rel_categories__id__exact=1'},
            )},
            {'title': '分类管理', 'perm': self.get_model_perm(UserInfo, 'change'), 'menus':(
                {'title': '主要分类', 'url': self.get_model_url(UserInfo, 'changelist') + '?_p_date__isnull=True'},
                {'title': '游戏资料', 'url': self.get_model_url(UserInfo, 'changelist') + '?_rel_parent__id__exact=2'},
            )},
        )

site.register(CommAdminView, AdminSettings)
