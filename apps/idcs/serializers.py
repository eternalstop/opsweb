from rest_framework import serializers
from .models import Idc


class IdcsSerializers(serializers.Serializer):
	"""
	Idcs 序列化类
	"""
	default_error_messages = {
		'required': '这个字段为必要字段.',
		'null': '这个字段不能为空.',
	}
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True,
	                             max_length=32,
	                             label="机房名称",
	                             help_text="机房完整名称",
	                             error_messages={
		                             "blank": "这个字段不能为空.",
		                             "required": "这个字段为必要字段.",
	                             }
	                             )
	address = serializers.CharField(required=True,
	                                max_length=256,
	                                label="机房地址",
	                                help_text="机房详细地址",
	                                error_messages={
		                                "blank": "这个字段不能为空.",
		                                "required": "这个字段为必要字段.",
	                                }
	)
	phone = serializers.CharField(required=True,
	                              max_length=15,
	                              label="联系电话",
	                              help_text="机房联系人电话",
	                              error_messages={
		                              "blank": "这个字段不能为空.",
		                              "required": "这个字段为必要字段.",
	                              }
	                              )
	email = serializers.EmailField(required=True,
	                               label="Email地址",
	                               help_text="机房联系人Email地址",
	                               error_messages={
		                               "blank": "这个字段不能为空.",
		                               "required": "这个字段为必要字段.",
	                               }
	                               )
	letter = serializers.CharField(required=True,
	                               max_length=5,
	                               label="机房字母简称",
	                               help_text="机房字母简称",
	                               error_messages={
		                               "blank": "这个字段不能为空.",
		                               "required": "这个字段为必要字段.",
	                               }
	                               )

	def create(self, validated_data):
		return Idc.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.address = validated_data.get('address', instance.address)
		instance.phone = validated_data.get('phone', instance.phone)
		instance.email = validated_data.get('email', instance.email)
		instance.letter = validated_data.get('letter', instance.letter)
		instance.save()
		return instance
