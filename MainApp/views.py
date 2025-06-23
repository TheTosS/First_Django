from django.core.exceptions import ObjectDoesNotExist
from django.db.models.fields import return_None
from django.shortcuts import render, HttpResponse, redirect
from django.template.context_processors import request

from MainApp.models import Item
from django.http import HttpResponseNotFound
items = [...]




# Create your views here.

def home(request):
    context = {"name" : "Roman",
               "surname" : "Erm"
    }
    return render(request, 'index.html', context)


def about(request):
    text = "<h1>About Page</h1>"
    return HttpResponse(text)

def items_list(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, 'items.html',context )

def item_page(request , id):
    try:
        item =Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse("Item not found")

    context = {
        "item": item

    }
    return render(request, 'item.html', context)

def item_add(request):
    if request.method == "GET": # вернем страницу с формой
     return render(request, 'create_item.html')
    elif request.method == "POST": # данные от формы
            name = request.POST.get("name")
            brand = request.POST.get("brand")
            count = request.POST.get("count")
            description = request.POST.get("description")
            item = Item(name=name, brand=brand, count=count, description=description)
            item.save()
            return redirect('items')




