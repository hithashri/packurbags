from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="customer")
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=300, null=True)
    price = models.FloatField()
    no_of_days = models.IntegerField()
    places_included = models.CharField(max_length=300 , null=True)
    image = models.ImageField(null= True, blank=True)
    name = models.CharField(max_length=300, null=True)
    info = models.TextField(null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null= True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=300, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    


class OrderItem(models.Model):
    package=models.ForeignKey(Package, on_delete=models.SET_NULL, blank=True, null=True)
    oder=models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    # def my_view(request):
    #     if request.method == 'POST':
    #         quantity = request.POST.get('quantity')

    @property
    def get_total(self):
        total = self.package.price * self.quantity
        return total

    def no_of_items(self):
        return self.quantity

    

class TravellerDetails(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, blank = True, null = True)
    name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    gender = models.CharField(max_length = 1, null = True)
    address = models.CharField(max_length = 400, null = True)
    date_of_birth = models.DateField(auto_now_add = True)

    def _str_(self):
        return self.address
