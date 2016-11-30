from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^contracts/$', views.getall, name="getall"),
	url(r'^contracts/create_contract/$', views.create_contract, name="create_contract"),
	url(r'^contracts/update_contract_form/(?P<pk>[0-9]+)/$', views.update_contract_form, name="update_contract_form"),
	url(r'^contracts/update_contract$', views.update_contract, name="update_contract"),
	url(r'^contracts/delete_contract/(?P<pk>[0-9]+)/$', views.delete_contract, name="delete_contract"),
]