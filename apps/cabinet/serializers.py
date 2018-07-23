from rest_framework import serializers
from idcs.models import Idc
from idcs.serializers import IdcsSerializers
from .models import Cabinet


class CabinetSerializer(serializers.Serializer):
	"""
	机柜序列化类
	"""
	idc = serializers.PrimaryKeyRelatedField(many=False, queryset=Idc.objects.all(), help_text="所在机房")
	name = serializers.CharField(required=True,
	                             max_length=255,
	                             label="机柜名称",
	                             help_text="机柜名称",
	                             error_messages={
		                             "blank": "这个字段不能为空.",
		                             "required": "这个字段为必要字段.",
	                             })

	def to_representation(self, instance):
		idc_obj = instance.idc
		ret = super(CabinetSerializer, self).to_representation(instance)
		ret["idc"] = {
			"id": idc_obj.id,
			"name": idc_obj.name
		}
		return ret

	def to_internal_value(self, data):
		"""
		反序列化第一步：拿到的是提交过来的原始数据：QueryDict => request.GET,request.POST
		"""
		return super(CabinetSerializer, self).to_internal_value(data)

	def create(self, validated_data):
		return Cabinet.objects.create(**validated_data)