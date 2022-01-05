from django.db import models


# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    costperitem = models.DecimalField(max_digits=10, decimal_places=2)
    stockquantity = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField(null=True)

    def calc_volume(self):
        volume = self.costperitem * self.stockquantity
        return volume

    def save(self, *args, **kwargs):
        self.volume = self.calc_volume()
        super(products, self).save()


