
from django.urls import path, include

# import views

from . import views

urlpatterns = [
    path('',views.landing,name="landing"),
    path('index', views.index, name="indexpage"),
    path('sign',views.sign,name="sign"),
    path('text',views.text,name="text"),
    path('sign1',views.sign1,name="sign1"),
    path('text1',views.text1,name="text1"),
    path('back',views.back,name="back"),
    path('runcode', views.runcode, name="runcode"),
    
    #####################################

    path('runOnVoiceCommand',views.runOnVoiceCommand,name="runOnVoiceCommand")

    #####################################
]