from http.client import HTTPResponse
from django.shortcuts import render
from .models import Category,Sales_man,Bill,Item,Invoice
from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import date


import time
# Create your views here.


def adminpanel(request):
   
    return render(request,'pages/adminpanel.html')


def addproduct(request):
    category=Category.objects.all()
    data={
        'category':category
    }
    return render(request,'pages/addproduct.html',data)

def billingpage(request):
    slman=Sales_man.objects.all()
    item=Item.objects.all()
    data={
        'salesman':slman,
        'items':item
    }
    return render(request,'pages/billingpage.html',data)
    
def reports(request):
    bl=Bill.objects.raw("SELECT DISTINCT date_of_purchase,id FROM billing_Bill")
    data={
        'tab':bl
    }
    return render(request,'pages/reports.html',data)


def repor(request):
    dt = request.GET.get("date")
    bl=Bill.objects.filter(date_of_purchase=dt)
    data={
        'tab':bl,
        'bt':dt
    }
    return render(request,'pages/repor.html',data)

def reportinvo(request):
    dt = request.GET.get("invnum")
    request.session['invoice_number']=dt
    
    return invoice(request)



def addcategory(request):
    return render(request,'pages/addcategory.html')

def addsalesman(request):
    return render(request,'pages/addsalesman.html')
def invoice(request):
    invoice_number=request.session['invoice_number']
    arr=Bill.objects.filter(invoice_number=invoice_number)
    jn=arr[0].item_name.split(",")
    arlenth=len(jn)
  
    data={
        'arr':arr,
        'jn':jn,
        'arlen':arlenth
        
        
    
        
        
    }
    return render(request,'pages/invoice.html',data)

def CategPost(request):
    if request.method == 'POST':
        name=request.POST['category']

        cat=Category(name=name)
        cat.save()
        messages.success(request, 'Category Added.')
        return redirect('addcategory')

def SalesmanPost(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']

        slman=Sales_man(name=name,phone_number=phone)
        slman.save()
        return redirect('addsalesman')
    
def ItemPost(request):
    if request.method=='POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        category = request.POST['category']
        price = request.POST['price']

        itm=Item(name=name,quantity=quantity,category=category,price=price)
        itm.save()
        return redirect('addproduct')

    

def BillPost(request):
    if request.method=='POST':

                invnum=Invoice.objects.get(id=1)

                invoice_number=int(invnum.number)+1
                invnum.number=invoice_number
                invnum.save()

                item_na=request.POST['item_name']+" "
                today = date.today()

                
                credit_or_not=request.POST['credit_or_not']
                total_amount=request.POST['total_amount']
                customer_name=request.POST['customer_name']
                phone_number=request.POST['phone_number']
                sales_man=request.POST['sales_man']
                request.session['invoice_number']=invoice_number
                bp=Bill(credit_or_not=credit_or_not,invoice_number=invoice_number,item_name=item_na,total_amount=total_amount,customer_name=customer_name,phone_number=phone_number,sales_man=sales_man,date_of_purchase=today)
                bp.save()
                it=item_na.split(",")
                itlen=len(it) - 1
                a={}
                for i in range(0,itlen):
                    a[i]=it[i].split("||")
                dicta={}
                for i in range(0,itlen):
                    q=a[i][0]
                    w=int(a[i][1])
                    if q in dicta:
                        dicta[q]+=w
                    else:
                        dicta[q]=w
                for i in dicta:
                    upd=Item.objects.get(name=str(i))
                    k=int(upd.quantity)
                    val=k-int(dicta[i])
                    upd.quantity=val
                    upd.save()
                    
                    
                
                return redirect('invoice')
            
                
            
        
        
