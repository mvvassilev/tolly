from django.db import models


class Item(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Storage(models.Model):
    objects = models.Manager()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item.name


    def stack(self, added_item):
        for storage_item in Storage.objects.all():
            if storage_item.item.name == added_item.item.name:
                storage_item.quantity += added_item.quantity
                Storage.objects.delete(pk=added_item.id)


    def add_item(self, added_item, amount):
        s = Storage(item=added_item, quantity=amount)
        s.save()
        for storage_item in Storage.objects.all():
            if storage_item.item.name == added_item.name:
                storage_item.quantity += amount
                s.delete()
        return f'Item added: {added_item.name}   Quantity:{amount}'


    def delete_item(self, item_id):
        storage_item = Storage.objects.filter(id=item_id)
        storage_item.delete()
        return f'Item deleted: {storage_item.name}'


    def search_item(self, item_id):
        return Storage.objects.filter(id=item_id)
        