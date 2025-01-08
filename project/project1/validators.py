from django.core.exceptions import ValidationError
# ------------------------------------------------------------------------------------------
from .models import *
# ------------------------------------------------------------------------------------------
import string


# 1 - validator:
# "username" validator: username uchun bir nechta shartlar berilgan validator:
# 1 - shart: username avval ro`yxatdan o`tmagan bo`lishi kerak;
# 2 - shart: username 50 ta simvoldan ortiq bo`lmasligi kerak;
def user_valid(value):
    if User.objects.filter(username=value).exists():
        raise ValidationError(
            "Bu foydalanuvchi nomi allaqachon ro'yxatdan o'tgan. Iltimos, boshqa foydalanuvchi nomini tanlang.")    
    if len(value) >= 50:
        raise ValidationError(
            "Username 50 ta simvoldan ortib ketdi"
        )
# ------------------------------------------------------------------------------------------

# 2 - validator:
# "password" validator: password uchun bir nechta shartlar berilgan validator: 
# 1 - shart: password son bilan boshlanmasligi kerak;
# 2 - shart: password faqat sonlar va harflardan tashkil topgan bo`lishi kerak;
# 3 - shart: password 8 ta sivmoldan kam va 15 ta simvoldan ortiq bo`lmasligi kerak;
def password_vali(value):
    if value[0].isdigit():
        raise ValidationError("Password boshi harf bilan boshlanishi kerak")
    
    if not all(char.isalnum() for char in value):
        raise ValidationError("Password faqat sonlar va harflardan tashkil topgan bo'lishi kerak")
    
    if len(value) < 8 or len(value) > 15:
        raise ValidationError("Password uzunligi 8 ta simvoldan kam va 15 ta simvoldan ko'p bo'lmasligi kerak")
# ------------------------------------------------------------------------------------------

# 3 - validator:
# "type name" validator: type name uchun bir nechta shartlar berilgan:
# 1 - shart: kiritilgan tur nomi oldin kiritilmagan bo`lishi kerak;
def type_name(value):
    if Type1.objects.filter(name=value).exists():
        raise ValidationError("Bunday tur nomi allaqachon qo'shilgan.")
# ------------------------------------------------------------------------------------------

# 4 - validator: 
# "flower name" validator: flower name uchun bir nechta shartlar berilgan:
# 1 - shart: kiritilgan gul nomi oldin kiritilmagan bo`lishi kerak;
def flower_name(value):
    if Flower.objects.filter(name=value).exists():
        raise ValidationError("Bunday ma'lumot allaqachon qo'shilgan.")
# ------------------------------------------------------------------------------------------


def homework_length(value):
    length = len(value)
    if length < 5:
        raise ValidationError("Uyga vazifa matni kamida 5 ta belgidan iborat bo'lishi kerak.")
    elif length > 1000:
        raise ValidationError("Uyga vazifa matni uzunligi 1000 ta belgidan oshmasligi zarur.")


# --- register --- #
