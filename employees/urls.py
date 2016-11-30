from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^employees/$', views.getall, name="getall"),
	url(r'^employees/create_employee_form/$', views.create_employee_form, name="create_employee_form"),
	url(r'^employees/create_employee/$', views.create_employee, name="create_employee"),
	url(r'^employees/update_employee_form/(?P<pk>[0-9]+)/$', views.update_employee_form, name="update_employee_form"),
	url(r'^employees/update_employee$', views.update_employee, name="update_employee"),
	url(r'^employees/delete_employee/(?P<pk>[0-9]+)/$', views.delete_employee, name="delete_employee"),
	url(r'^employees/search_schedule/$', views.search_schedule, name="search_schedule"),
	url(r'^employees/schedule_employee/(?P<pk>[0-9]+)/$', views.schedule_employee, name="schedule_employee"),
	url(r'^employees/create_schedule_form/(?P<pk>[0-9]+)/$', views.create_schedule_form, name="create_schedule_form"),
	url(r'^employees/create_schedule/$', views.create_schedule, name="create_schedule"),
	url(r'^employees/update_schedule_form/(?P<pk>[0-9]+)/$', views.update_schedule_form, name="update_schedule_form"),
	url(r'^employees/update_schedule$', views.update_schedule, name="update_schedule"),
	url(r'^signin/$', views.signin, name="signin"),
	url(r'^logout$', auth_views.logout, {'next_page': '/'}, name='logout'),
]
