from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Item, Storage

def index(request):
    items_list = Item.objects.all()
    context = {'items_list' : items_list}
    return  render(request, 'items/index.html', context)

def storage(request):
    storage_items = Storage.objects.all()
    items_list = Item.objects.all()
    context = {'storage_items' : storage_items, 'items_list' : items_list}
    return render(request, 'items/storage.html', context)


def regitems(request):
    items_list = Item.objects.all()
    context = { 'items_list' : items_list}
    return render(request, 'items/regitems.html', context)

#filter by item_code
def filter(request, item_code):
    item = Item.objects.filter(pk=item_code)
    return render(request, 'items/{{ item.name }}.html', {'item': item})
