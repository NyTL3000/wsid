from django.shortcuts import render, redirect
from .models import products_collection

# Create your views here.
from django.http import HttpResponse
def home (request):
    return  render (request, "pages/homePage.html" )
def about (request): 
    return render(request, "pages/aboutPage.html" )
def products (request): 
    products = products_collection.find() 
    return render(request, "pages/blogPage.html" ,{'products': products}  )
def products_details (request, products_slug):
    products_details = products_collection.find_one({"slug": products_slug})
    return render(request, "pages/blog_details.html",
    {'products_details': products_details})
def custom_404(request, exception):
    return render(request, 'pages/404.html', {}, status=404)
def product (request): 
    products = products_collection.find() 
    return render(request, "manager/products.html",{'products': products} )
def manager (request): 
    return render(request, "manager/manager.html" )

def add_product(request):
    if request.method == 'POST':
        title =request.POST.get('title')
        price =int(request.POST.get('price',0))
        image =request.POST.get('image')

        new_products = {
            "title":title,
            "price":price,
            "image":image,
            
        }
        products_collection.insert_one(new_products)
    return redirect("/manager/products")

def edit_product(request, product_name):
    query_filter ={"id": product_name}
    if request.method == 'POST':
        if request.POST.get('_method') == 'PUT':
            title =request.POST.get('title')
            price =int(request.POST.get('price',0))
            image =request.POST.get('image')
            new_products = {
            "title":title,
            "price":price,
            "image":image, }

            products_collection.find_one_and_update({"title": product_name},
                {'$set': new_products}
             )
            
    return redirect("/manager/products")

def delete_product(request,product_name):
    if request.method == 'POST':
       products_collection.delete_one({"title": product_name})

                                
    return redirect("/manager/products")
    