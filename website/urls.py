from django.urls import path
from . import views
urlpatterns = [
    path('',views.csvtowats,name="home"),
    path('csvfields',views.csvfields,name="csvfields"),
]