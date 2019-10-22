from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Item

def index(request):
    items_list = Item.objects.all()
    context = { 'items_list' : items_list}
    return  render(request, 'items/index.html', context)