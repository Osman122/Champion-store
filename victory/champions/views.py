from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse 
from champions.forms import ProductForm
from django.contrib.auth.decorators import login_required


# products = [
#     {"id":1, "name":"pistole", "image":"pic1.png"},
#     {"id":2, "name":"swaard", "image":"pic2.png"},
#     {"id":3, "name":"m24 gun", "image":"pic3.png"},
#     {"id":4, "name":"Akm gun", "image":"pic4.png"},
#     {"id":5, "name":"Akm gun", "image":"pic4.png"}
# ]
from champions.models import Product ,Category




def index(request):
    products = Product.objects.all()
    return render(request, 'champions/home.html',context={"products":products})


def about(request):
    return render(request, 'champions/about.html')


def contact(request):
    return render(request, 'champions/contact.html')


# def product(request, id):
#     theif = filter(lambda th:th['id']==id , products)  #
#     # print(theif)
#     theif = list(theif)
#     if theif:
#         print(theif[0])
#         return render(request,'champions/product.html',context= {"product":theif[0]})

#     return HttpResponse("Sorry target theif profile not found ")

def show(request,id):
      product = Product.objects.get(id=id)
      return render(request,'champions/product.html',context= {"product":product})


def delete(request,id):
      product = Product.objects.get(id=id)
      product.delete()
      url =reverse('home')
      return redirect(url)


def filter(request):
    
        name = request.GET.get('name')
    
        queryset = Product.objects.filter(name__startswith=name)
        print("=================",name,queryset)
        

        return render(request, 'champions/search.html', context={'queryset': queryset,"name":name})

@login_required
def add(request):
     
     form=ProductForm()

     if request.method =='POST':
         form=ProductForm(request.POST,request.FILES)
         if form.is_valid():
            name=request.POST['name']
            price=request.POST['price']
            category=form.cleaned_data['category']
            image = None
            if "image" in request.FILES :
                image = request.FILES['image']

            product =Product()
            product.name=name
            product.price=price
            product.image=image
            product.category=category
            product.owner=request.user
            
            product.save()
            print(request.POST)
            url=reverse('champion.product',args=[product.id])

            return redirect(url)
     
     return render(request  ,  "champions/forms/create.html",context={"form":form})

@login_required
def edit(request, id):
    
    product = get_object_or_404(Product, id=id) 
    if product.owner != request.user:
       
       return HttpResponse("You have to be the to edit this product.")
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
           

            # Check if a new image is provided
            if 'image' in request.FILES:
                product.image = form.cleaned_data['image']
            

            product.save()
            return redirect('home')
    else:
            form = ProductForm(initial={
            'name': product.name,
            'price': product.price,
            'image':product.image
            })

    context={"form":form}
    
    return render(request, 'champions/forms/edit.html',context )

def category_list(request): 
    categories = Category.objects.all() 
    context = { 'categories': categories} 
    return render(request, 'champions/category.html',context )


def category_detail(request, category): 
    products = Product.objects.filter(category__name=category) 
    context = { 'products': products, 'category': category } 
    return render(request, 'champions/categoryitems.html', context)
