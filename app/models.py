from django.db import models

# Create your models here.
class Productcategory(models.Model):
    cname=models.CharField(max_length=100,primary_key=True)
    cid=models.IntegerField()
    def __str__(self):
        return self.cname
    
class Product(models.Model):
    cname=models.ForeignKey(Productcategory,on_delete=models.CASCADE)
    pid=models.IntegerField()
    pname=models.CharField(max_length=100)
    pprice=models.IntegerField()
    date=models.DateField()
    def __str__(self):
        return self.pname
    