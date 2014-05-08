# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
import datetime


# Create your models here.
class Server(models.Model):
	id_number = models.IntegerField(u'ID(変更禁止)',primary_key=True)
	domain_name = models.CharField(u'ドメイン名',max_length=200, null=True, blank=True)
	race_domain_name = models.CharField(u'RACEﾄﾞﾒｲﾝ名',max_length=200, null=True, blank=True)
	#items = models.CharField('種目(変更禁止)',max_length=200, null=True, blank=True)
	items = models.ForeignKey(u'Items', null=True, blank=True)
	domain_register_day = models.DateField(u'ドメイン登録日', null=True, blank=True)
	domain_change_day = models.DateField(u'ドメイン変更日', null=True, blank=True)
	domain_delete_day = models.DateField(u'ドメイン削除日', null=True, blank=True)
	domain_validity_day = models.DateField(u'ドメイン有効期限', null=True, blank=True)
	end_day = models.DateField(u'終了日', null=True, blank=True)
	use_host_name = models.CharField(u'利用ホスト名',max_length=200, null=True, blank=True)
	domain_ip = models.CharField(u'ドメイン用IP',max_length=200, null=True, blank=True)
	dns1_hostname = models.CharField(u'DNS1(ホスト名)',max_length=200, null=True, blank=True)
	dns1_ip = models.CharField(u'DNS1(IP)',max_length=200, null=True, blank=True)
	dns2_hostname = models.CharField(u'DNS2(ホスト名)',max_length=200, null=True, blank=True)
	dns2_ip = models.CharField(u'DNS2(IP)',max_length=200, null=True, blank=True)
	#conditions = models.CharField(u'状態',max_length=200, null=True, blank=True)
	conditions = models.ForeignKey(u'Conditions', null=True, blank=True)
	# CONDITIONS_CHOICES = (
	# 			(0, u'運用中'),
	# 			(1, u'解約'),
	# )
	# conditions = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

	ftp_account = models.CharField(u'FTPアカウント',max_length=200, null=True, blank=True)
	ftp_password = models.CharField(u'FTPパスワード',max_length=200, null=True, blank=True)
	#registrar = models.CharField(u'レジストラ',max_length=200, null=True, blank=True)
	registrar = models.ForeignKey(u'Registrar', null=True, blank=True)
	company_name = models.CharField(u'会社名',max_length=200, null=True, blank=True)
	post_name = models.CharField(u'部署名',max_length=200, null=True, blank=True)
	charge_name = models.CharField(u'担当者名',max_length=200, null=True, blank=True)
	company_address = models.CharField(u'住所',max_length=200, null=True, blank=True)
	telephone_number = models.CharField(u'TEL',max_length=200, null=True, blank=True)
	facsimile_number = models.CharField(u'FAX',max_length=200, null=True, blank=True)
	info_mail_address = models.CharField(u'通知用Mail',max_length=200, null=True, blank=True)
	sainet_charge = models.CharField(u'弊社担当',max_length=200, null=True, blank=True)
	#sainet_charge = models.ForeignKey('Sainet_charge')

	manage_url = models.CharField(u'管理用URL',max_length=200, null=True, blank=True)
	manage_user_name = models.CharField(u'管理画面ユーザ名',max_length=200, null=True, blank=True)
	manage_password = models.CharField(u'管理画面パスワード',max_length=200, null=True, blank=True)
	mail_admin_pass = models.CharField(u'MailAdminPass',max_length=200, null=True, blank=True)
	demand_company_name = models.CharField(u'請求会社名',max_length=200, null=True, blank=True)
	demand_charge_name = models.CharField(u'請求氏名',max_length=200, null=True, blank=True)
	demand_address = models.CharField(u'請求住所',max_length=200, null=True, blank=True)
	manage_ip_address = models.CharField(u'管理用IPアドレス',max_length=200, null=True, blank=True)
	login_account = models.CharField(u'ログインアカウント',max_length=200, null=True, blank=True)
	login_password = models.CharField(u'ログインパスワード',max_length=200, null=True, blank=True)
	vmware_esxi = models.CharField(u'VMware Esxi',max_length=200, null=True, blank=True)
	machine_name = models.CharField(u'マシン名',max_length=200, null=True, blank=True)

	#追加項目
	manage_conn_info = models.CharField(u'管理ページへの接続情報',max_length=200, null=True, blank=True)
	data_store_place = models.CharField(u'データストアの場所',max_length=200, null=True, blank=True)
	ssl_response_code = models.CharField(u'SSLチャレンジレスポンスコード',max_length=200, null=True, blank=True)
	database_spec = models.CharField(u'データベース仕様',max_length=200, null=True, blank=True)
	database_conn_id = models.CharField(u'データベース接続ID',max_length=200, null=True, blank=True)
	database_conn_pass = models.CharField(u'データベース接続PASS',max_length=200, null=True, blank=True)
	procedure_book_place = models.CharField(u'手順書の場所',max_length=200, null=True, blank=True)
	esxi_physics_host_name = models.CharField(u'ESXiの物理ホスト名',max_length=200, null=True, blank=True)
	esxi_physics_host_ip = models.CharField(u'ESXiの物理ホストIP',max_length=200, null=True, blank=True)
	server_rack_place = models.CharField(u'ラックの場所',max_length=200, null=True, blank=True)

	# register_day = models.DateField(u'登録日', null=True, blank=True)
	# change_day = models.DateField(u'変更日', null=True, blank=True)
	# delete_day = models.DateField(u'削除日', null=True, blank=True)

	def __unicode__(self):
		return self.domain_name
	class Meta:
		verbose_name = u'サーバ'

#状態（運用中・解約）
class Items(models.Model):
	items = models.IntegerField(u'ID',primary_key=True)
	#conditions_name = models.CharField(u'状態',max_length=200,primary_key=True)
	items_name = models.CharField(u'種目(変更禁止)',max_length=200)
	def __unicode__(self):
		return self.items_name

#状態（運用中・解約）
class Conditions(models.Model):
	conditions = models.IntegerField(u'ID',primary_key=True)
	#conditions_name = models.CharField(u'状態',max_length=200,primary_key=True)
	conditions_name = models.CharField(u'状態',max_length=200)
	def __unicode__(self):
		return self.conditions_name

#レジストラ（JPRS・お名前.com）
class Registrar(models.Model):
	registrar = models.IntegerField(u'ID',primary_key=True)
	registrar_name = models.CharField(u'レジストラ',max_length=200)
	def __unicode__(self):
		return self.registrar_name

#弊社担当者（社員名）
# class Sainet_charge(models.Model):
# 	sainet_charge = models.IntegerField('ID',primary_key=True)
# 	sainet_charge_name = models.CharField('弊社担当',max_length=200)
# 	def __unicode__(self):
# 		return self.sainet_charge_name

# class Demand_company(models.Model):
# 	demand_company = models.IntegerField(u'ID',primary_key=True)
# 	demand_company_name = models.CharField(u'請求会社名',max_length=200,primary_key=True)
# 	def __unicode__(self):
# 		return self.demand_company_name