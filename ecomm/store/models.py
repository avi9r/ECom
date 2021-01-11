from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField( max_length=100)
    disp= models.CharField( max_length=300)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    colour = models.ManyToManyField('Colour')
    price = models.IntegerField()
    discount = models.IntegerField()
    date = models.DateField()
    image= models.ImageField(upload_to='store/images')

    def __str__(self):
     return self.name
    

class Category(models.Model):
    cat_id =models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField(max_length=50)
    disc= models.CharField( max_length=300)
    image= models.ImageField(upload_to='store/images')

    def __str__(self):
     return self.name

class SubCategory(models.Model):
    sub_cat_id =models.AutoField(db_column='BID', primary_key=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    disc= models.CharField( max_length=300)
    
    image= models.ImageField(upload_to='store/images')

    def __str__(self):
     return self.name

class Colour(models.Model):
    colour_id = models.AutoField(db_column='BID', primary_key=True)
    colour = models.CharField(max_length=50)

    def __str__(self):
     return self.colour

class Customer(models.Model):
    customer_id = models.AutoField(db_column='BID', primary_key=True)
    fname = models.CharField( max_length=100)
    lname = models.CharField( max_length=100)
    email= models.CharField( max_length=100)
    mobile = models.IntegerField()
    password= models.CharField( max_length=50)
    city = models.CharField( max_length=100)
    pin = models.IntegerField()
    addesss =models.CharField( max_length=200)
    shiping_city = models.CharField( max_length=100)
    shiping_pin = models.IntegerField()
    shiping_addesss =models.CharField( max_length=200)

    def __str__(self):
     return self.fname+" "+self.lname

class Order(models.Model):
    order_id = models.AutoField(db_column='BID', primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price =models.PositiveIntegerField()
    payment_mode = models.CharField(max_length=50)
    order_date = models.DateField( auto_now=False, auto_now_add=False)
    ship_date = models.DateField( auto_now=False, auto_now_add=False)
    payment_status = models.BooleanField()

    def __str__(self):
     return self.order_id+" "+self.product


