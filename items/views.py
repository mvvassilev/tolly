from django.shortcuts import render
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


def item_filter(request, item_code):
    item = Item.objects.filter(pk=item_code)
    context = {'item': item}
    return render(request, 'items/{{ item.name }}.html', context)


def storage_filter(request, item_code):
    s = Storage.objects.filter(id=item_code)
    item = s.item
    context = {'item': item}
    return render(request, 'items/storage.html', context)


def add_item(request, added_item, amount):
    s = Storage.objects.filter(pk=added_item.id)
    s.quantity += amount
