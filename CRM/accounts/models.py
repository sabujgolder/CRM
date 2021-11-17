from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=128,null=True)
    phone = models.CharField(max_length = 200,null = True)
    image = models.ImageField(upload_to='profile_pics',null=True,default='default.jpg')
    email = models.EmailField(max_length=200,null=True)
    date_created = models.DateTimeField(null=True,auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (('Indoor','Indoor'),
                ('Out Door', 'OutDoor'))

    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(max_length=200,null=True)
    image = models.ImageField(upload_to='product_image',null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
            ('Pending','Pending'),
            ('Out For Delivery','Out For Delivery'),
            ('Delivered','Delivered')
    )

    customer = models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null=True,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        return self.product.name
