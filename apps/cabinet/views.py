from django.shortcuts import render
from .serializers import CabinetSerializer
from rest_framework import viewsets
from .models import Cabinet


# Create your views here.
class CabinetViewset(viewsets.ModelViewSet):
	"""
	retrieve:
		返回指定机柜信息
	list:
		返回机柜列表
	update:
		更新机柜信息
	destroy:
		删除机柜记录
	create:
		创建机柜记录
	partial_update:
		更新机柜部分字段
	"""
	queryset = Cabinet.objects.all()
	serializer_class = CabinetSerializer
