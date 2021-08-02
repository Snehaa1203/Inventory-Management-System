from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from. forms import *
from django.contrib.auth.models import User
from django.contrib import messages


@login_required(login_url='login')
def index(request):
	orders=Order.objects.all()
	products=Product.objects.all()
	staff_count=User.objects.all().count()
	orders_count=Order.objects.all().count()
	products_count=Product.objects.all().count()
	if request.method == 'POST':
	   form=OrderForm(request.POST)
	   if form.is_valid():
		   instance=form.save(commit=False)
		   instance.staff=request.user
		   instance.save()
		   return redirect('index')
	else:
		form=OrderForm()
	context={'orders':orders,
	'form': form,
	'products':products,
	'products_count':products_count,
	'orders_count':orders_count,
	'staff_count':staff_count,
	}
	return render(request,'index.html',context)

@login_required(login_url='login')
def staff(request):
	items=User.objects.all()
	context={"staff":items}
	return render(request,'staff.html',context)

@login_required(login_url='login')
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
		   product_name=form.cleaned_data.get('name')
		   messages.success(request,f'{product_name} has been added')
		   return redirect('product')
	else:
		form=ProductForm()
	context={
		'items':items,
		'form':form
	}
	return render(request,'product.html',context)

@login_required(login_url='login')
def product_delete(request,pk):
	item=Product.objects.get(id=pk)
	if request.method =='POST':
		item.delete()
		return redirect('product')
	return render(request,'product_delete.html')

@login_required(login_url='login')
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