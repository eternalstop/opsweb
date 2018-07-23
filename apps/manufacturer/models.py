from django.db import models


# Create your models here.
class Manufacturer(models.Model):
	vendor_name = models.CharField("厂商名称", max_length=32, db_index=True, unique=True, help_text="厂商名称")
	tel = models.CharField("联系电话", null=True, max_length=15, help_text="联系电话")
	email = models.CharField("Email地址", null=True, max_length=64, help_text="邮件地址")
	remark = models.CharField("备注", null=True, max_length=320, help_text="备注")

	def __str__(self):
		return self.vendor_name

	class Meta:
		db_table = "resource_manufaturer"
		ordering = ["id"]


class ProductModel(models.Model):
	model_name = models.CharField("产品型号", null=True, max_length=32, help_text="产品型号")
	vendor = models.ForeignKey(Manufacturer, verbose_name="所属制造商", help_text="所属制造商")

	def __str__(self):
		return self.model_name

	class Meta:
		db_table = "resource_productmodel"
		ordering = ["id"]
