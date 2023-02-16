from django.contrib import admin
from .models import Item,Bill,Sales_man,Category,Invoice
from django.utils.html import format_html
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display=('id','name','category','quantity','price')
    list_display_links=('id','name')

class InvoiceAdmin(admin.ModelAdmin):
    list_display=('id','number')
    list_display_links=('id','number')
class CatAdmin(admin.ModelAdmin):
    list_display=('id','name')
    list_display_links=('id','name')

class SalesmanAdmin(admin.ModelAdmin):
    list_display=('id','name','phone_number')
    list_display_links=('id','name')

class BillAdmin(admin.ModelAdmin):
    list_display=('id','invoice_number','customer_name','item_name','date_of_purchase','sales_man','phone_number')
    list_display_links=('id','invoice_number','customer_name','date_of_purchase')


admin.site.register(Item,ItemAdmin,)
admin.site.register(Bill,BillAdmin)
admin.site.register(Sales_man,SalesmanAdmin)
admin.site.register(Category,CatAdmin)
admin.site.register(Invoice,InvoiceAdmin)