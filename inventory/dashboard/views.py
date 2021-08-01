from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from. forms import *
from django.contrib.auth.models import User


@login_required(login_url='login')
def index(request):
	return render(request,'index.html')

@login_required(login_url='login')
def staff(request):
	items=User.objects.all()
	context={"staff":items}
	return render(request,'staff.html',context)

def staff_detail(request,pk):
	item=User.objects.get(id=pk)
	context={"staff":item}
	return render(request,"staff_detail.html",context)

@login_required(login_url='login')
def product(request):
	items=Product.objects.all()
	if request.method == 'POST':
	   form=ProductForm(request.POST)
	   if form.is_valid():
		   form.save()
		   return redirect('product')
	else:
		form=ProductForm()
	context={
		'items':items,
		'form':form
	}
	return render(request,'product.html',context)

def product_delete(request,pk):
	item=Product.objects.get(id=pk)
	if request.method =='POST':
		item.delete()
		return redirect('product')
	return render(request,'product_delete.html')

def product_update(request,pk):
	item=Product.objects.get(id=pk)
	if request.method =='POST':
	   form=ProductForm(request.POST,instance=item)
	   if form.is_valid():
		   form.save()
		   return redirect('product')
	else:
		  form=ProductForm(instance=item)
	context={'form':form}
	return render(request,'product_update.html',context)

@login_required(login_url='login')
def order(request):
	orders=Order.objects.all()
	context={'orders':orders}
	return render(request,'order.html',context)