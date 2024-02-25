from django.db import models

# Create your models here.

class CompanyInformation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE) 
    image = models.ImageField(null = True)
    price= models.FloatField(null = True)
    date = models.DateField(auto_now_add=True, null = True)
    
    def __str__(self) -> str:
        return self.product_name
    
class About(models.Model):
    abouthead = models.CharField( max_length=100)
    aboutdescription = models.TextField()
    ourteam = models.CharField(max_length=100)
    OurGoal = models.TextField(null=True)
    Plan = models.CharField( max_length=50,null=True)
    

    def __str__(self) -> str:
        return self.abouthead
    
class Contact(models.Model):
    To = models.CharField( max_length=50)
    email = models.CharField(max_length=50)
    Number = models.CharField( max_length=50)

    def __str__(self) -> str:
        return self.To
