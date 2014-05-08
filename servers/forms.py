# -*- coding: utf-8 -*-
from django.forms import *
from servers.models import Server,Conditions,Registrar

class ServerSearchForm(Form):
	domain_name = CharField(min_length=2, max_length=100,required=False)
	company_name = CharField(min_length=2, max_length=100,required=False)
#   publish_date = forms.DateField(required=False)

class ServerForm(ModelForm):
	#ID
	id_number = IntegerField(
		widget=DateInput(attrs={'placeholder':'001'}))
	#ドメイン名
	domain_name = CharField(
		widget=DateInput(attrs={'placeholder':'sainet.ne.jp'}),required=False)
	#RACEﾄﾞﾒｲﾝ名
	race_domain_name = CharField(
		widget=DateInput(attrs={'placeholder':'XXX.XXX.XXX'}),required=False)
	#種目(変更禁止)
	# items = CharField(
	# 	widget=DateInput(attrs={'placeholder':'カスタマイズ'}),required=False)
	#ドメイン登録日
	domain_register_day = DateField(
		#widget=DateInput(attrs={'placeholder':'1998-07-06','class':'input-large','id':'datepicker1'}))
		widget=DateInput(attrs={'placeholder':'1998-07-06','id':'datepicker1'}),required=False)
	#ドメイン変更日
	domain_change_day = DateField(
		widget=DateInput(attrs={'placeholder':'1998-07-06','id':'datepicker2'}),required=False)
	#ドメイン削除日
	domain_delete_day = DateField(
		widget=DateInput(attrs={'placeholder':'1998-07-06','id':'datepicker3'}),required=False)
	#ドメイン有効期限
	domain_validity_day = DateField(
		widget=DateInput(attrs={'placeholder':'1998-07-06','id':'datepicker4'}),required=False)
	#終了日
	end_day = DateField(
		widget=DateInput(attrs={'placeholder':'1998-07-06','id':'datepicker5'}),required=False)
	#利用ホスト名
	use_host_name = CharField(
		widget=DateInput(attrs={'placeholder':'sainet.ne.jp'}),required=False)
	#ドメイン用IP
	domain_ip = CharField(
		widget=DateInput(attrs={'placeholder':'XXX.XXX.XXX.XXX'}),required=False)
	#DNS1(ホスト名)
	dns1_hostname = CharField(
		widget=DateInput(attrs={'placeholder':'sainet.ne.jp'}),required=False)
	#DNS1(IP)
	dns1_ip = CharField(
		widget=DateInput(attrs={'placeholder':'XXX.XXX.XXX.XXX'}),required=False)
	#DNS2(ホスト名)
	dns2_hostname = CharField(
		widget=DateInput(attrs={'placeholder':'sainet.ne.jp'}),required=False)
	#DNS2(IP)
	dns2_ip = CharField(
		widget=DateInput(attrs={'placeholder':'XXX.XXX.XXX.XXX'}),required=False)
	#状態
	# conditions = CharField(
	# 	widget=DateInput(attrs={'placeholder':'XXX.XXX.XXX.XXX'}),required=False)
	#FTPアカウント
	ftp_account = CharField(
		widget=DateInput(attrs={'placeholder':'kensyu'}),required=False)
	#FTPパスワード
	ftp_password = CharField(
		widget=DateInput(attrs={'placeholder':'sainet'}),required=False)
	#レジストラ
	# registrar = CharField(
	# 	widget=DateInput(attrs={'placeholder':'XXX.XXX.XXX.XXX'}),required=False)
	#会社名
	company_name = CharField(
		widget=DateInput(attrs={'placeholder':'株式会社井上商事'}),required=False)
	#部署名
	post_name = CharField(
		widget=DateInput(attrs={'placeholder':'情報システム部'}),required=False)
	#担当者名
	charge_name = CharField(
		widget=DateInput(attrs={'placeholder':'井上一郎'}),required=False)
	#住所
	company_address = CharField(
		widget=DateInput(attrs={'placeholder':'埼玉県川口市並木2丁目25番3号'}),required=False)
	#TEL
	telephone_number = CharField(
		widget=DateInput(attrs={'placeholder':'048-259-2366'}),required=False)
	#FAX
	facsimile_number = CharField(
		widget=DateInput(attrs={'placeholder':'048-259-2870'}),required=False)
	#通知用Mail
	info_mail_address = CharField(
		widget=DateInput(attrs={'placeholder':'info@sainet.or.jp'}),required=False)
	#弊社担当
	sainet_charge = CharField(
	 	widget=DateInput(attrs={'placeholder':'XXX.XXX.XXX.XXX'}),required=False)
	#管理用URL
	manage_url = CharField(
		widget=DateInput(attrs={'placeholder':'sainet.or.jp/admin/'}),required=False)
	#管理ユーザ名
	manage_user_name = CharField(
		widget=DateInput(attrs={'placeholder':'root'}),required=False)
	#管理パスワード
	manage_password = CharField(
		widget=DateInput(attrs={'placeholder':'admin'}),required=False)
	#MailAdminPass
	mail_admin_pass = CharField(
		widget=DateInput(attrs={'placeholder':'mailadmin'}),required=False)
	#請求会社名
	demand_company_name = CharField(
		widget=DateInput(attrs={'placeholder':'株式会社井上ホールディングス'}),required=False)
	#請求氏名
	demand_charge_name = CharField(
		widget=DateInput(attrs={'placeholder':'井上次郎'}),required=False)
	#請求住所
	demand_address = CharField(
		widget=DateInput(attrs={'placeholder':'埼玉県川口市並木2丁目25番3号'}),required=False)
	#管理用IPアドレス
	manage_ip_address = CharField(
		widget=DateInput(attrs={'placeholder':'XXX.XXX.XXX.XXX'}),required=False)
	#ログインアカウント
	login_account = CharField(
		widget=DateInput(attrs={'placeholder':'loginadmin'}),required=False)
	#ログインパスワード
	login_password = CharField(
		widget=DateInput(attrs={'placeholder':'sainet'}),required=False)
	#VMware Esxi
	vmware_esxi = CharField(
		widget=DateInput(attrs={'placeholder':'VMware'}),required=False)
	#マシン名
	machine_name = CharField(
		widget=DateInput(attrs={'placeholder':'dataserver'}),required=False)

	#ｰｰｰｰｰｰｰｰｰｰｰｰｰ追加項目
	#管理ページへの接続情報
	manage_conn_info = CharField(
		widget=DateInput(attrs={'placeholder':'管理ページへの接続情報'}),required=False)
	#データストアの場所
	data_store_place = CharField(
		widget=DateInput(attrs={'placeholder':'データストアの場所'}),required=False)
	#SSLチャレンジレスポンスコード
	ssl_response_code = CharField(
		widget=DateInput(attrs={'placeholder':'SSLチャレンジレスポンスコード'}),required=False)
	#データベース仕様
	database_spec = CharField(
		widget=DateInput(attrs={'placeholder':'データベース仕様'}),required=False)
	#データベース接続ID
	database_conn_id = CharField(
		widget=DateInput(attrs={'placeholder':'データベース接続ID'}),required=False)
	#データベース接続PASS
	database_conn_pass = CharField(
		widget=DateInput(attrs={'placeholder':'データベース接続PASS'}),required=False)
	#手順書の場所
	procedure_book_place = CharField(
		widget=DateInput(attrs={'placeholder':'手順書の場所'}),required=False)
	#ESXiの物理ホスト名
	esxi_physics_host_name = CharField(
		widget=DateInput(attrs={'placeholder':'ESXiの物理ホスト名'}),required=False)
	#ESXiの物理ホストIP
	esxi_physics_host_ip = CharField(
		widget=DateInput(attrs={'placeholder':'ESXiの物理ホストIP'}),required=False)
	#ラックの場所
	server_rack_place = CharField(
		widget=DateInput(attrs={'placeholder':'ラックの場所'}),required=False)
	class Meta:
		model = Server
#任意項目
#required=False

# class Sainet_chargeForm(ModelForm):
# 	class Meta:
# 		model = Sainet_charge

class RegistrarForm(ModelForm):
	class Meta:
		model = Registrar