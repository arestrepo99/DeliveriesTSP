from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)
    
    def to_html(self):
        return self.__str__()

class Client(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    def __str__(self):
        return f'{str(self.name)}, {str(self.address)}'
    
    def to_html(self):
        return self.__str__()

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def get_products(self):
        try:
            products = ', '.join([str(op) for op in OrderProduct.objects.filter(order=self)])
        except (OrderProduct.DoesNotExist):
            products = "NA"
        return products

    def to_html(self):
        return f'<h4>{str(self.client.name)}</h4> <small class="text-muted">{self.get_products()}</small>'

    def __str__(self):
        return f'{str(self.client.name)}, {self.get_products()}'

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('order', 'product')
    
    def __str__(self):
        return f' {self.product}: {self.quantity}'
    
    def to_html(self):
        return self.__str__()

# product1 = Product.objects.create()
# product2 = Product.objects.create()
# my_order = Order.objects.create(email='foo@bar.com')
# OrderProduct.objects.create(product=product1, order=my_order)
# OrderProduct.objects.create(product=product2, order=my_order, quantity=14)