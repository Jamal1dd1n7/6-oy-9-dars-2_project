from django.db import models

class Type1(models.Model):
    name = models.CharField(max_length=100)  
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nomi')
    photo = models.ImageField(upload_to="post/photos/", null=True, blank=True)
    type1 = models.ForeignKey(Type1, on_delete=models.CASCADE, related_name='flowers')  
    color = models.CharField(max_length=50, blank=True, null=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) 
    production_date = models.DateField(blank=True, null=True)  

    def __str__(self):
        return self.name
