from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from .models import Category, Product, ProductImages
from django.db import connection
from django.http import JsonResponse


# Create your views here.


def Base(response):
    return render(response, "CommerceAdmin/base.html", {})


def AddProduct(response):
    if response.is_ajax():
        AllCat = Category.objects.all()
        if response.method == "POST":
            print(response.POST)
            title = response.POST.get('title')
            description = response.POST.get("description")
            price = response.POST.get("price")
            tags = response.POST.get("tttaaggg")
            category = int(response.POST.get("cat"))
            stock = response.POST.get("stock")
            Brand = response.POST.get("Brand")
            size = response.POST.get("sssiiizzee")
            color = response.POST.get("colorss")
            product = Product(
                title=title,
                description=description,
                category=Category.objects.get(id=category),
                Price=int(price),
                Stock=int(stock),
                Brand=Brand,
                tags=tags,
                sizes=size,
                colors=color
            )
            product.save()
            images = response.FILES.getlist("upload_imgs[]")
            for image in images:
                primage = ProductImages(image=image, product=product)
                primage.save()
        return render(response, "CommerceAdmin/AddProduct.html", {"category": AllCat})
    return render(response, "CommerceAdmin/base.html", {})


def UpdateProduct(response, id):
    if response.method == "POST":
        title = response.POST.get('title')
        description = response.POST.get("description")
        price = response.POST.get("price")
        tags = response.POST.get("tttaaggg")
        category = int(response.POST.get("cat"))
        stock = response.POST.get("stock")
        Brand = response.POST.get("Brand")
        size = response.POST.get("sssiiizzee")
        color = response.POST.get("colorss")
        pros = Product.objects.filter(id=id)
        if pros:
            cat = Category.objects.get(id=category)
            pro = Product.objects.get(id=id)
            pro.title = title
            pro.description = description
            pro.category = cat
            pro.Price = int(price)
            pro.Stock = int(stock)
            pro.Brand = Brand
            pro.tags = tags
            pro.sizes = size
            pro.colors = color
            pro.save()
            if response.FILES.getlist("upload_imgs[]"):
                image = ProductImages.objects.filter(product=pro)
                for img in image:
                    img.delete()
                images = response.FILES.getlist("upload_imgs[]")
                for image in images:
                    primage = ProductImages(image=image, product=pro)
                    primage.save()
            return JsonResponse({'data': True})
        else:
            return JsonResponse({'data': False})
    else:
        pro = Product.objects.filter(id=id)
        if pro:
            AllCat = Category.objects.all()
            pro = pro[0]
            image = ProductImages.objects.filter(product=pro)
            return render(response, "CommerceAdmin/UpdateProduct.html",
                          {"pro": pro, "image": image, "category": AllCat})
        else:
            return render(response, "CommerceAdmin/4O4.html")


def AllProducts(response):
    QueryLimit = 5
    numberOfProduct = Product.objects.all().count()
    count = numberOfProduct // QueryLimit
    remainder = numberOfProduct % QueryLimit
    if remainder > 0:
        count += 1

    return render(response, "CommerceAdmin/AllProducts.html",
                  {"maxval": count, "totalproduct": numberOfProduct, 'QueryLimit': QueryLimit})


def AllProductItems(response, count):
    QueryLimit = 5
    start = (QueryLimit * count) - QueryLimit
    end = (QueryLimit * count)
    pro = Product.objects.all()[start:end]
    ProList = []
    for i in pro:
        data = {
            'id': i.id,
            'title': i.title[:36],
            'Active': True,
            'count': 0,
            'item_image': ProductImages.objects.filter(product=i)[:1][0].image,
        }
        ProList.append(data)
    return render(response, "CommerceAdmin/AllproductItems.html", {'data': ProList})


def AddCategory(response):
    if response.method == "POST":
        if response.POST.get('Record') == 'New':
            cat = Category(
                Name=response.POST.get('category'),
                Picture=response.FILES.get('upload_imgs[]'),
                Active=True
            )
            cat.save()
        if response.POST.get('Record') == 'ACTIVE':
            cat = Category.objects.get(id=response.POST.get('id'))
            if cat.Active:
                cat.Active = False
            else:
                cat.Active = True
            cat.save()
        elif response.POST.get('Record') == 'Other':
            cat = Category.objects.get(id=response.POST.get('id'))
            if response.FILES.get('upload_imgs[]'):
                cat.Picture = response.FILES.get('upload_imgs[]')
            cat.Name = response.POST.get('category')
            cat.save()
    list = []

    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM count_cat_view''')
    for result in cursor.fetchall():
        data = {
            'id': result[0],
            'name': result[1],
            'item_image': Category.objects.get(id=result[0]).Picture,
            'Active': result[3],
            'count': result[4],
        }
        list.append(data)

    return render(response, "CommerceAdmin/AddCategory.html", {'data': list})


def Orders(response):
    return render(response, "CommerceAdmin/Orders.html")


def DasBoard(response):
    return render(response, "CommerceAdmin/DasBoard.html")


def Seacrh(response, data):
    Query = '''SELECT title FROM commerceadmin_product WHERE '''
    lenth = len(data.split(" ")) - 1
    for num, word in enumerate(data.split(" ")):
        if num < lenth:
            Query = Query + f"title  LIKE '%{word}%' AND "
        else:
            Query = Query + f"title  LIKE '%{word}%'  "
    cursor = connection.cursor()
    cursor.execute(Query)
    list = []
    for result in cursor.fetchall():
        res = result[0].lower()
        for word in data.split(" "):
            if len(word) > 1:
                res = res.replace(word.lower(), f"<b>{word.lower()}</b>")
        list.append(res)
    return JsonResponse({'data': list})


def OrdersDetail(response):
    allpro = [
        {
            'url': "https://static-01.daraz.pk/p/c5428d27497c99e681d11e53634200a7.jpg_340x340q80.jpg_.webp",
            'title': "Small Gift Bags with Ribbon Handles",
            'quan': 2,
            'price': "1500Rs",
            'date': "1/1/2021",
            'color': "#00ffff",
            'size': "X",
        }, {
            'url': "https://static-01.daraz.pk/p/c5428d27497c99e681d11e53634200a7.jpg_340x340q80.jpg_.webp",
            'title': "Small Gift Bags with Ribbon Handles",
            'quan': 2,
            'price': "1500Rs",
            'date': "1/1/2021",
            'color': "#00ffff",
            'size': "X",
        }, {
            'url': "https://static-01.daraz.pk/p/c5428d27497c99e681d11e53634200a7.jpg_340x340q80.jpg_.webp",
            'title': "Small Gift Bags with Ribbon Handles",
            'quan': 2,
            'price': "1500Rs",
            'date': "1/1/2021",
            'color': "#00ffff",
            'size': "X",
        },

    ]
    total = {
        'quan': 6,
        'price': "4500Rs",
    }
    return render(response, "CommerceAdmin/OrdersDetail.html", {'allpro': allpro, 'total': total})
