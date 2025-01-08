from django.db import models
from PIL import Image
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Type1 model: 
class Type1(models.Model):
    # name model: tur nomini kiritish uchun model; maksimal 100 ta simvol kiritish mumkin;
    name = models.CharField(max_length=100) 
    # description model: turga ta`rif berish uchun model; sivmol kiritish cheklanmagan; 
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
# --------------------------------------------------------------------------------------------------

class Flower(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nomi')
    photo = models.ImageField(upload_to="post/photos/", null=True, blank=True)
    type1 = models.ForeignKey(Type1, on_delete=models.CASCADE, related_name='flowers')  
    color = models.CharField(max_length=50, blank=True, null=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) 
    production_date = models.DateField(blank=True, null=True)  

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Matni")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Muallif")
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name="Gul nomi")
    created = models.DateTimeField(auto_now_add=models.CASCADE, verbose_name="Yaratilgan")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Izoh "
        verbose_name_plural = "Izohlar"
        ordering = ['-id']
