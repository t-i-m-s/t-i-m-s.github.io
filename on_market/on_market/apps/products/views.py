from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Product
# Create your views here.
#====================================================побочные функции
def sort_func(lest,frm,to):
	if frm and int(frm) > lest[len(lest) - 1].price:
		return []
	elif frm == '' and to:
		for p in lest:
			if p.price > int(to):
				lest = lest[0:lest.index(p)]
				break
		return lest
	elif to == '' and frm:
		for p in lest:
			if p.price >= int(frm):
				lest = lest[lest.index(p):len(lest)]
				break
		return lest
	elif frm and to:
		for p in lest:
			if p.price >= int(frm):
				lest = lest[lest.index(p):len(lest)]
				break
		for p in lest:
			if p.price > int(to):
				lest = lest[0:lest.index(p)]
				break
		return lest
	else:
		return lest

def category_func(product):

	product_list = []
	tags_list = []
	for p in product:
		product_list.append(p.category)

	tags_list.append(product_list[0])
	count = 0
	while True:
		for p in product_list:
			for tag in tags_list:
				if p != tag:
					count += 1
				if count == len(tags_list):
					tags_list.append(p)
					break
			product_list.remove(p)
			count = 0
			break
		if len(product_list) == 0:
			break
	return tags_list#функция для поиска тэгов и передачи их в списке другим функциям
#====================================================действующие функции
def main_page(request):

	product = Product.objects.order_by('price')
	tags_list = category_func(product)

	return render(request, 'main_page.html', {'product': product, 'tags_list': tags_list})

def show_product(request, product_id):

	product = Product.objects.get(id = product_id)
	return render(request, 'product_page.html', {'product': product})

def category(request, category):

	product = Product.objects.order_by('price')
	tags_list = category_func(product)
	product_category = Product.objects.filter(category = category)

	return render(request, 'product_category_page.html', {'product': product_category, 'tags_list': tags_list, 'category': category})

def sort(request):
	#request.POST['password'] request.POST['min']
	#return HttpResponseRedirect(reverse('articles:detail', args = (a.id,)))
	#product = Product.objects.order_by('price')
	#return HttpResponse(product[0].inf()['price'])

	sortbutton = request.POST['sortbutton']
	frm = request.POST['from']
	to = request.POST['to']

	product = []
	orig_product = Product.objects.order_by('price')
	tags_list = category_func(Product.objects.order_by('price'))# тэги товаров
	for i in orig_product:
		product.append(i)
	if len(product) > 0:
		if sortbutton == 'max':
			product = sort_func(product,frm,to)
			product.reverse()
			if len(product) > 0:
				return render(request,'main_page.html',{'product': product, 'value': {'from': frm,'to': to}, 'tags_list': tags_list})
			else:
				return render(request,'main_page_not_found.html', {'tags_list': tags_list})
		else:
			product = sort_func(product,frm,to)
			if len(product) > 0:
				return render(request,'main_page.html',{'product': product, 'value': {'from': frm,'to': to}, 'tags_list': tags_list})
			else:
				return render(request,'main_page_not_found.html', {'tags_list': tags_list})
	else:
		return render(request,'main_page_not_found.html', {'tags_list': tags_list})
	#return HttpResponse(product[0].product_name)
	#return render(request,'main_page.html',{'product':product}

def sort_in_categories(request, category):
	#request.POST['password'] request.POST['min']
	#return HttpResponseRedirect(reverse('articles:detail', args = (a.id,)))
	#product = Product.objects.order_by('price')
	#return HttpResponse(product[0].inf()['price'])

	sortbutton = request.POST['sortbutton']
	frm = request.POST['from']
	to = request.POST['to']

	product = []
	orig_product = Product.objects.order_by('price')
	tags_list = category_func(Product.objects.order_by('price'))# тэги товаров
	for i in orig_product:
		if i.category == category:
			product.append(i)
	if len(product) > 0:
		if sortbutton == 'max':
			product = sort_func(product,frm,to)
			product.reverse()
			if len(product) > 0:
				return render(request,'product_category_page.html',{'product': product, 'value': {'from': frm,'to': to}, 'tags_list': tags_list, 'category': category})
			else:
				return render(request,'main_page_not_found.html', {'tags_list': tags_list})
		else:
			product = sort_func(product,frm,to)
			if len(product) > 0:
				return render(request,'product_category_page.html',{'product': product, 'value': {'from': frm,'to': to}, 'tags_list': tags_list, 'category': category})
			else:
				return render(request,'main_page_not_found.html', {'tags_list': tags_list})
	else:
		return render(request,'main_page_not_found.html', {'tags_list': tags_list})
	#return HttpResponse(product[0].product_name)
	#return render(request,'main_page.html',{'product':product}