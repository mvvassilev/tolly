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


    def delete_item(self, item_id):
        storage_item = Storage.objects.filter(id=item_id)
        storage_item.delete()
        return f'Item deleted: {storage_item.name}'


    def search_item(self, item_id):
        return Storage.objects.filter(id=item_id)
        