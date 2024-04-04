from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('home',views.home, name='home'),
    path('report',views.report,name='report'),
    path('add_record',views.add_record,name='add_record'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('signout',views.signout, name='signout'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
]
