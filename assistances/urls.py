from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
url(r'^assistances_taking/$', views.redirect_assistance_taking, name="redirect_assistance_taking"),
url(r'^assistances/validate_code_employee/$', views.validate_code_employee, name="validate_code_employee"),
url(r'^assistances/search_assistances/$', views.search_assistances, name="search_assistances"),
url(r'^assistances/employee_assistances/(?P<pk>[0-9]+)/$', views.employee_assistances, name="employee_assistances"),
]