from django.urls import path
from newchallange import views

urlpatterns = [

    path('<int:month>', views.monthly_chall_numeric),
    path('<str:month>/', views.monthly_challanges, name='month-challange'),
    path('', views.home, name="home"), # /challange/
]