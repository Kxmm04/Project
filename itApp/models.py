from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, default='', primary_key=True)
    desc = models.CharField(max_length=200, default='')
        
    def __str__(self):
            return str(self.name) 
        
class Computer(models.Model):
    comid = models.CharField(max_length=13, default='', primary_key=True)
    processor = models.CharField(max_length=200, default='')
    graphic = models.CharField(max_length=200, default='')
    display = models.CharField(max_length=200, default='')
    ram = models.CharField(max_length=200, default='')
    Storage = models.CharField(max_length=200, default='')
    OS = models.CharField(max_length=200, default='')
    battery = models.CharField(max_length=200, default='')
    warranty = models.CharField(max_length=200, default='')
    weight = models.CharField(max_length=200, default='')
    price = models.FloatField(default=0.0)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='static/images/Computer', default=None)
    net = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.comid )
    


class Storage (models.Model):
    storageid = models.CharField(max_length=13, default='', primary_key=True)
    name = models.CharField(max_length=200, default='')
    model = models.CharField(max_length=200, default='')
    brand = models.CharField(max_length=200, default='')
    RPM = models.CharField(max_length=200, default='')
    Form_Factor = models.CharField(max_length=200, default='')
    Random_Write = models.CharField(max_length=200, default='')
    Random_Read = models.CharField(max_length=200, default='')
    Sequential_Write = models.CharField(max_length=200, default='')
    Sequential_Read = models.CharField(max_length=200, default='')
    interface = models.CharField(max_length=200, default='')
    technology = models.CharField(max_length=200, default='')
    size_ssd = models.CharField(max_length=200, default='')
    storage = models.CharField(max_length=200, default='')
    price = models.FloatField(default=0.0)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='static/images/Storage', default=None)
    net = models.IntegerField(default=0)
    warranty = models.CharField(max_length=200, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.storageid)
    
class Accessories(models.Model):
    accid = models.CharField(max_length=13, default='', primary_key=True)
    brand = models.CharField(max_length=200, default='')
    model = models.CharField(max_length=200, default='')
    color = models.CharField(max_length=200,default='')
    keyswitch = models.CharField(max_length=200, default='')
    keypresslifetime= models.CharField(max_length=200, default='')
    numberkey = models.CharField(max_length=200, default='')
    mediakey = models.CharField(max_length=200, default='')
    interface  = models.CharField(max_length=200, default='')
    weight = models.CharField(max_length=200, default='')
    price = models.FloatField(default=0.0)
    size = models.IntegerField(default=0)  # Allowing empty values in this field
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='static/images/Accessories', default=None)
    net = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.accid) 

    