from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('index',views.index),
    path('home/',views.home,name= "home"),
    path('logout/',views.logout,name="logout"),
    path('addclient/', views.addclient, name="addclient"),
    path('addequepment/', views.addequepment, name="addequepment"),
    path('addplant/', views.addplant, name="addplant"),
    path('addproject/', views.addproject, name="addproject"),
    path('addwherehouse/', views.addwherehouse, name="addwherehouse"),
    path('vclient',views.vclient,name = "vclient"),
    path('vequepment',views.vequepment,name="vequepment"),
    path('vplant',views.vplant,name = "vplant"),
    path('vproject',views.vproject,name="vproject"),
    path('vwherehouse',views.vwherehouse,name="vwherehouse"),
    path('addregisterEquipment',views.registerequipment,name="registerequipement"),
    path('returnEquipment',views.returnequipmant,name="returnequipment"),
    path('assignEquipment',views.assign,name = "assigenequipment"),
    path('addsite',views.addsite,name = "addsite")
]