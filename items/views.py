from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Item

def index(request):
    items_list = Item.objects.all()
    context = { 'items_list' : items_list}
    return  render(request, 'items/index.html', context)

#filter by item_code
def filter(request, item_code):
    item = Item.objects.filter(pk=item_code)
    return render(request, 'items/{{ item.name }}.html', {'item': item})