from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect

from .models import Item, Storage


def index(request):
    items_list = Item.objects.all()
    context = {'items_list': items_list}
    return render(request, 'items/index.html', context)


def storage(request):
    storage_items = Storage.objects.all()
    items_list = Item.objects.all()
    context = {'storage_items': storage_items, 'items_list': items_list}
    return render(request, 'items/storage.html', context)


def regitems(request):
    items_list = Item.objects.all()
    context = {'items_list': items_list}
    return render(request, 'items/regitems.html', context)

# filter by item_code


def item_filter(request):
    item = Item.objects.filter(pk=item_code)
    context = {'item': item}
    return render(request, 'items/{{ item.name }}.html', context)


def storage_filter(request):
    s = Storage.objects.filter(id=item_code)
    item = s.item
    context = {'item': item}
    return render(request, 'items/storage.html', context)


def add_item(request):
    storage_items = Storage.objects.all()
    items_list = Item.objects.all()

    added_item_name = request.POST.get('added_item_name')
    added_item_quantity = request.POST.get('added_item_quantity')

    item = Item.objects.filter(name=added_item_name)
    storage_item = Storage.objects.get(item=item[0])
    storage_item.quantity += int(added_item_quantity)
    storage_item.save()

    context = {
        'storage_items': storage_items,
        'items_list': items_list
    }
    return render(request, 'items/storage.html', context)
