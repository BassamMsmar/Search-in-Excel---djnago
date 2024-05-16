from django.urls import path
from .views import shipment_list, inoices_list, upload_file

urlpatterns = [
    path('', shipment_list, name='shipmetns_list'),
    path('inoices/', inoices_list, name='inoices_list'),
    path('inoices/add', upload_file, name='upload_file'),
]