from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index')
]
from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('update/<int:id1>/<int:id2>', views.update, name='update'),
  path('update/<int:id>/updaterecord/<int:id1>/<int:id2>', views.updaterecord, name='updaterecord'),
]