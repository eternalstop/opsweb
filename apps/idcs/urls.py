from django.conf.urls import url, include
from idcs import views
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register('list', views.IdcViewset)
# route.register('detail', views.IdcDetail)


urlpatterns = [
	url(r'^', include(route.urls)),
]
