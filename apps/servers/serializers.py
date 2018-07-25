from rest_framework import serializers
from .models import Servers, NetworkDevice, IP
from .models import Manufacturer, ProductModel


class ServersAutoReportSerializer(serializers.Serializer):
	"""
	服务器信息自动同步序列化
	"""
	ip = serializers.IPAddressField(required=True)
	hostname = serializers.CharField(required=True, max_length=32)
	cpu = serializers.CharField(required=True, max_length=64)
	memory = serializers.CharField(required=True, max_length=32)
	disk = serializers.CharField(required=True, max_length=256)
	os = serializers.CharField(required=True, max_length=32)
	sn = serializers.CharField(required=True, max_length=64)
	manufacturer = serializers.CharField(required=True)
	model_name = serializers.CharField(required=True)
	uuid = serializers.CharField(required=True, max_length=32)
	network = serializers.JSONField(required=True)

	def validate_manufacturer(self, value):
		try:
			return Manufacturer.objects.get(vendor_name__exact=value)
		except Manufacturer.DoesNotExist:
			return self.create_manufacturer(value)

	def validate(self, attrs):
		manufacturer_obj = attrs["manufacturer"]
		try:
			manufacturer_obj.producymodel_set.filter(model_name_exact=attrs["model_name"])
		except ProductModel.DoesNotExist:
			self.create_product_model(manufacturer_obj, attrs["model_name"])
		return attrs

	def create(self, validated_data):
		network = validated_data.pop["network"]
		server_obj = Servers.objects.create(**validated_data)
		self.check_server_network_device(network, server_obj)
		return server_obj

	def check_server_network_device(self, network, server_obj):
		"""
		检查指定服务器有没有这些网卡设备，并作关联
		"""
		network_device_queryset = server_obj.networkdevice_set.all()
		for device in network:
			try:
				network_Device_obj = network_device_queryset.get(name__exact=device["name"])
			except NetworkDevice.DoesNotExist:
				self.check_server_network_device(server_obj, device)

	def check_ip(self, network_device_obj, ifnets):
		ip_queryset = network_device_obj.ip_set.all()
		for ifnet in ifnets:
			try:
				ip_queryset.get(ip_addr__exact=ifnet["ip_addr"])
			except IP.DoesNotExist:
				ip_obj = self.create_ip(network_device_obj, ifnet)

	def create_ip(self, network_device_obj, ifnet):
		ifnet["device"] = network_device_obj
		return IP.objects.create(**ifnet)

	def create_network_device(self, server_obj, device):
		ips = device.pop("ips")
		device["host"] = server_obj
		network_device_obj = NetworkDevice.objects.create(**device)
		self.check_ip(network_device_obj, ips)
		return network_device_obj

	def create_manufacturer(self, vendor_name):
		return Manufacturer.objects.create(vendor_name=vendor_name)

	def create_product_model(self, manufacturer, model_name):
		return ProductModel.objects.create(model_name=model_name, vendor=manufacturer)
	# class Meta:
	# 	model = Servers
	# 	fields = ("ip", "hostname", "cpu", "memory", "disk", "os", "sn", "manufacturer", "model_name", "uuid")

	def to_representation(self, instance):
		ret = {
			"hostname": instance.hostname,
			"ip": instance.ip
		}
		return ret


class ServerSerializer(serializers.ModelSerializer):
	"""
	服务器序列化
	"""
	class Meta:
		model = Servers
		fields = "__all__"


class NetworkDeviceSerializer(serializers.ModelSerializer):
	"""
	网卡序列化
	"""
	class Meta:
		model = NetworkDevice
		fields = "__all__"


class IPSerializer(serializers.ModelSerializer):
	"""
	IP序列化
	"""
	class Meta:
		model = IP
		fields = "__all__"
