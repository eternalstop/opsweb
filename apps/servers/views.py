from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from .models import Servers, NetworkDevice, IP
from .serializers import ServersAutoReportSerializer, NetworkDeviceSerializer, IPSerializer, ServerSerializer


class ServerAutoReportViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
	"""
	create:
		创建服务器记录
	"""
	queryset = Servers.objects.all()
	serializer_class = ServersAutoReportSerializer


class ServerViewset(viewsets.ReadOnlyModelViewSet):
	"""
	retrieve:
		返回指定网卡信息
	list:
		返回网卡列表
	"""
	queryset = Servers.objects.all()
	serializer_class = ServerSerializer


class NetworkDeviceViewset(viewsets.ReadOnlyModelViewSet):
	"""
	retrieve:
		返回指定网卡信息
	list:
		返回网卡列表
	"""
	queryset = NetworkDevice.objects.all()
	serializer_class = NetworkDeviceSerializer


class IPViewset(viewsets.ReadOnlyModelViewSet):
	"""
	retrieve:
		返回指定IP信息
	list:
		返回IP列表
	"""
	queryset = IP.objects.all()
	serializer_class = IPSerializer