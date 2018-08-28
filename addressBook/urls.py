from django.conf.urls import url
from . import views

app_name = 'addressbook'

urlpatterns = [
    url(r'^new/$', views.newAddress_view, name='newaddress'),
    url(r'', views.addressBook_view, name='addressbook'),
]