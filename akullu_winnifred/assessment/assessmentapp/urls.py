from . import views
from django.urls import path


#urls here
urlpatterns = [
    path('',views.index,name='index')
]
