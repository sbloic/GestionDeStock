from django.db import models

class Gestion(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    cost_per_item = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    quantity_in_stock = models.IntegerField(null=False, blank=False)
    quantity_sold = models.IntegerField(null=False, blank=False)
    sales = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    stock_date = models.DateField(auto_now_add=True)
    last_sales = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name +" PROGISSA"

    def update_stock(self):
        if self.pk is not None:
            old_gestion = Gestion.objects.get(pk=self.pk)
            if self.quantity_sold > old_gestion.quantity_sold:
                diff = self.quantity_sold - old_gestion.quantity_sold
                self.quantity_in_stock -= diff

    def save(self, *args, **kwargs):
        self.sales = self.cost_per_item * self.quantity_sold
        self.update_stock()
        super(Gestion, self).save(*args, **kwargs)






