from django.urls import path, re_path

from . import views
app_name = 'car_app'

urlpatterns = [
    
    path ('api/car/create/',views.CarCreateApiView.as_view(), name='cars_create'),
    path ('api/car/list/',views.CarListApiView.as_view(), name='cars_read'),
    path ('api/car/update/<pk>/',views.CarUpdateView.as_view(), name='cars_read'),
    path ('api/car/delete/<pk>/',views.CarDeleteView.as_view(), name='cars_delete'),

    
]



