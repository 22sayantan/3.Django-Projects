from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    purchase_date = models.DateField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10,decimal_places=2,editable=False)

    def save(self,*args,**kargs):
        self.total_cost = self.quantity * self.price
        super(Purchase,self).save(*args,**kwargs)

        def __str__(self):
            return f"{self.product.name} Purchase (ID: {self.id})"
