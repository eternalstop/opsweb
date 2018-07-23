from django.db import models
from manufacturer.models import Manufacturer, ProductModel
from idcs.models import Idc
from cabinet.models import Cabinet


# # Create your models here.
class Servers(models.Model):
	ip = models.CharField("管理IP", max_length=15, db_index=True, unique=True, help_text="管理IP")
	hostname = models.CharField("主机名", max_length=32, db_index=True, unique=True, help_text="主机名")
	cpu = models.CharField("CPU", max_length=64, help_text="CPU")
	memory = models.CharField("运行内存", max_length=32, help_text="运行内存")
	disk = models.CharField("磁盘", max_length=256, help_text="磁盘")
	os = models.CharField("操作系统", max_length=32, help_text="操作系统")
	sn = models.CharField("SN", max_length=64, db_index=True, help_text="SN")
	manufacturer = models.ForeignKey(Manufacturer, verbose_name="制造商", help_text="制造商")
	model_name = models.ForeignKey(ProductModel, verbose_name="服务器型号", help_text="服务器型号")
	consle_ip = models.CharField("远程管理卡IP", max_length=15, db_index=True, unique=True, help_text="远程管理卡IP")
	idc = models.ForeignKey(Idc, null=True, verbose_name="所在机房", help_text="所在机房")
	cabinet = models.ForeignKey(Cabinet, null=True, verbose_name="所在机柜", help_text="所在机柜")
	cabinet_position = models.CharField("机柜位置", null=True, max_length=32, help_text="机柜位置")
	uuid = models.CharField("UUID", db_index=True, unique=True, max_length=32, help_text="UUID")
	last_check = models.DateTimeField("检测时间", db_index=True, auto_now=True, help_text="检测时间")
	remark = models.CharField("备注", null=True, max_length=256, help_text="备注")

	def __str__(self):
		return self.ip

	class Meta:
		db_table = "resource_servers"
		ordering = ["id"]


class NetworkDevice(models.Model):
	"""
	网卡模型
	"""
	name = models.CharField("网卡设备名", max_length=32, help_text="网卡设备名")
	mac_addr = models.CharField("MAC地址", max_length=64, help_text="MAC地址")
	host = models.ForeignKey(Servers, verbose_name="所在服务器", help_text="所在服务器")
	remark = models.CharField("备注", null=True, max_length=256, help_text="备注")

	def __str__(self):
		return self.name

	class Meta:
		db_table = "resource_network_device"
		ordering = ["id"]


class IP(models.Model):
	"""
	IP模型
	"""
	ip_addr = models.CharField("ip地址", max_length=15, db_index=True, unique=True, help_text="ip地址")
	netmask = models.CharField("子网掩码", max_length=15, help_text="子网掩码")
	device = models.ForeignKey(NetworkDevice, verbose_name="所在网卡", help_text="所在网卡")
	gateway = models.CharField("网关", max_length=15, help_text="网关")
	remark = models.CharField("备注", null=True, max_length=256, help_text="备注")

	def __str__(self):
		return self.ip_addr

	class Meta:
		db_table = "resource_ip"
		ordering = ["id"]


