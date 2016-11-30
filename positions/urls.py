from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^positions/$', views.getall, name="getall"),
	url(r'^positions/create_position_form/$', views.create_position_form, name="create_position_form"),
	url(r'^positions/create_position/$', views.create_position, name="create_position"),
	url(r'^positions/update_position_form/(?P<pk>[0-9]+)/$', views.update_position_form, name="update_position_form"),
	url(r'^positions/update_position$', views.update_position, name="update_position"),
	url(r'^positions/delete_position/(?P<pk>[0-9]+)/$', views.delete_position, name="delete_position"),
]