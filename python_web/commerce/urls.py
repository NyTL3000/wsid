from django.urls import path
from commerce import views 
app_name="commerce"


urlpatterns= [ 
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("blog/",views.products,name="blog"),
    path("products/<slug:products_slug>",
         views.products_details,
         name="products_details"),
    path("manager/products",views.product,name="product"),
    path("manager/",views.manager,name="manager"),
    path("manager/add/products",views.add_product,name="add_products"),
    path("manager/edit/product/<str:product_name>", views.edit_product),
    path("manager/delete/products/<str:product_name>",views.delete_product,name="delete_products")
]
#  