
from django.urls import path

from . import views


app_name='ecommerceapp'
urlpatterns = [

    path('',views.Allprodcat,name='Allprodcat'),
    path('<slug:c_slug>/',views.Allprodcat,name='prod_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='prodetail'),

]
