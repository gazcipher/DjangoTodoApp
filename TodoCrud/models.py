from django.db import models

# Create your models here.

class Grocery(models.Model):
    itemName = models.CharField("Name of Item", max_length=255, blank = False, null = False)
    itemDescription = models.CharField("Description of Item", max_length=1000, blank = True, null = True)
    itemPrice = models.BigIntegerField("Price of Item", blank = False, null = False)
    createdOn = models.DateTimeField("Creation Date", auto_now_add=True)

    def __str__(self):
        return self.itemName
