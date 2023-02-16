from django.urls.resolvers import URLPattern
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    
    path('',views.adminpanel,name="adminpanel"), 
    path('adminpanel',views.adminpanel,name="adminpanel"), 
    path('addproduct',views.addproduct,name="addproduct"), 
    path('billingpage',views.billingpage,name="billingpage"), 
    path('reports',views.reports,name="reports"), 
    path(r'd',views.repor), 
    path(r'h',views.reportinvo), 
    path('addcategory',views.addcategory,name="addcategory"), 
    path('addsalesman',views.addsalesman,name="addsalesman"), 
    path('CategPost',views.CategPost,name="CategPost"), 
    path('ItemPost',views.ItemPost,name="ItemPost"), 
    path('SalesmanPost',views.SalesmanPost,name="SalesmanPost"),
    path('BillPost',views.BillPost,name="BillPost"),
    path('invoice',views.invoice,name="invoice"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
