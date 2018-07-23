from rest_framework import serializers
from .models import Manufacturer, ProductModel


class ManufacturerSerializer(serializers.ModelSerializer):
	"""
	制造商序列化类
	"""
	class Meta:
		model = Manufacturer
		fields = "__all__"


class ProductModelSerializer(serializers.ModelSerializer):
	"""
	厂商序列化类
	"""
	class Meta:
		model = ProductModel
		fields = "__all__"

	def validate(self, attrs):
		manufactorer_obj = attrs["vendor"]
		model_name = attrs["model_name"]
		try:
			manufactorer_obj.producymodel_set.filter(model_name_exact=model_name)
			raise serializers.ValidationError("该型号已存在")
		except ProductModel.DoesNotExist:
			return attrs

	def to_representation(self, instance):
		vendor = instance.vendor
		ret = super(ProductModelSerializer, self).to_representation(instance)
		ret["vendor"] = {
			"id": vendor.id,
			"name": vendor.name
		}
