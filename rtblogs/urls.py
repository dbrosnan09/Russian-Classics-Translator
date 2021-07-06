from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('rtranslate/', views.rtranslate, name='rtranslate'),
    path('rtpicture/', views.rtpicture, name='rtpicture'),
    path('main_page/', views.main_page, name='main_page'),
    path('bk/', views.bk, name='bk'),
    path('pf/', views.pf, name='pf'),
    path('nu/', views.nu, name='nu'),
    path('idiot/', views.idiot, name='idiot'),
        path('demons/', views.demons, name='demons'),
        path('nhd/', views.nhd, name='nhd'),
           path('wp/', views.wp, name='wp'),
                      path('ak/', views.ak, name='ak'),
                          path('ispo/', views.ispo, name='ispo'),
                     path('dii/', views.dii, name='dii'),

]