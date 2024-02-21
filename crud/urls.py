from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('home',views.home, name='home'),
    path('report',views.report,name='report'),
    path('add_record',views.add_record,name='add_record'),
]
