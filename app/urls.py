from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('register',views.register,name='register'),
    path('pin',views.pin,name='pin'),
    path('checkbalance',views.checkBal,name='checkbalance'),
    path('deposit',views.deposit,name='deposit'),
    path('withdraw',views.withdraw,name='withdraw'),
    path('acc_transfer',views.acc_transfer,name='acc_transfer')
]