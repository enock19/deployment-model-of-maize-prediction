from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('record/database.html',views.record, name ='record'),
    path('download/excel',views.generate_excel,name='generate_excel'),  
]