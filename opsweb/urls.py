"""opsweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from idcs.views import IdcViewset
from rest_framework.routers import DefaultRouter
from users.views import UserViewset
from rest_framework.documentation import include_docs_urls
from cabinet.views import CabinetViewset
from manufacturer.views import ManufacturerViewset, ProductModelViewset
from servers.views import ServerViewset, NetworkDeviceViewset, IPViewset


route = DefaultRouter()
route.register('idcs', IdcViewset, base_name='idcs')
route.register('users', UserViewset, base_name='users')
route.register('cabinet', CabinetViewset, base_name='cabinet')
route.register('manufacturer', ManufacturerViewset, base_name='manufacturer')
route.register('productmodel', ProductModelViewset, base_name='productmodel')
route.register('servers', ServerViewset, base_name='servers')
route.register('networkdevice', NetworkDeviceViewset, base_name='networkdevice')
route.register('IP', IPViewset, base_name='IP')


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^', include(route.urls)),
    url(r'^docs/', include_docs_urls("opsweb运维平台接口文档")),
]
