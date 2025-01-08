from django import forms
from django.core.exceptions import ValidationError
# --------------------------------------------------------------------------------------------------------
from .validators import *
from .models import *


# type uchun form 
class TypeForm(forms.Form):
    # title form: tur nomini kiritish uchun form, maksimal 250 ta simvol yozish mumkin; 
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        "placeholder": "Nomi", # placeholder:  
        "class": "form-control" # class: 
    }), label='Nomi') # label:
    # --------------------------------------------------------------------------------------------------------
    # description form: turning tarifini yozish uchun form, simvol yozish cheklanmagan;
    description = forms.CharField(widget = forms.Textarea(attrs={
        "placeholder": "Ta`rif", # placeholder:
        "class": "form-control" # class:
    }), label="Ta`rif") # label:  
# --------------------------------------------------------------------------------------------------------

# flower uchun form 
class FlowerForm(forms.Form):
    # name form: gulning nomini kiritish uchun form, maksimal 250 ta simvol yozish mumkin;
    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        "placeholder": "Nomi", # placeholder: 
        "class": "form-control" # class: 
    }), label='Nomi') # label:
    # --------------------------------------------------------------------------------------------------------
    # photo form: gulning rasmini joylash uchun form;
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "form-control" # class: 
    }))
    # --------------------------------------------------------------------------------------------------------
    # type form: gulni turini tanlash uchun form;
    type1 = forms.ModelChoiceField(queryset=Type1.objects.all(), widget=forms.Select(attrs={
        "class": "form-select" # placeholder:
    }))
    # --------------------------------------------------------------------------------------------------------
    # color form: gulning rangini tanlash uchun form;
    color = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        "placeholder": "Rangi", # placeholder:
        "class": "form-control" # class: 
    }), required=False
    # yuqoridagi "required = False" qismi, agar gulning rangi qandayligi kiritilmasa ham form to`g`ri ishlashini bildiradi;
    )
    # --------------------------------------------------------------------------------------------------------
    # price form: gulning narxini kiritish uchun form;
    price = forms.IntegerField(widget=forms.TextInput(attrs={
        "placeholder": "Narxi" # placeholder:
    }))
    # --------------------------------------------------------------------------------------------------------
    # production_date form: gulning qaysi kuni sotuvga chiqarilganini vaqtini belgilash uchun form; 
    production_date =forms.TimeField(widget=forms.TimeInput(attrs={
        "placeholder": "Sotuvga chiqarilgan vaqti",
        "class": "form-control"
    }))
# --------------------------------------------------------------------------------------------------------

# Register uchun form
class RegisterForm(forms.Form):
    # username form: foydalanuvchi username ni kiritish uchun form, maksimal 50 ta simvol kiritish mumkin;
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-lg" # class: 
        }),
        label="Foydalanuvchi nomi", # label: 
        validators=[user_valid] 
        # validator: username uchun validator; bu validator, validators.py faylida yozilgan (5-17 column); 
    )
    # --------------------------------------------------------------------------------------------------------
    # email form: foydalanuvchi email kiritish uchun form: maksimal 100 ta simvol mumkin;
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': "form-control form-control-lg" # class:
        }),
        label="Elektron pochta manzili" # label: 
    )
    # --------------------------------------------------------------------------------------------------------
    # password form: foydalanuvchi password kiritish uchun form; password 8 ta simvoldan kam 15 ta simvoldan ko`p bo`lmasligi kerak;
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg" # class:
        }),
        label="Parol", # label:
        validators=[password_vali]
        # validator: password uchun validator; bu validator, validators.py faylida yozilgan(22-36 column)
    )
    # --------------------------------------------------------------------------------------------------------
    # confirm_password: foydalanuvchi kiritgan password ni qayta kiritish uchun form; 
    confirm_password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg" # class:
        }),
        label="Parolni qayta kiriting", # label:
        validators=[password_vali]
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Parollar bir-biriga mos kelmayapti. Iltimos, qayta tekshirib, to'g'ri kiriting!")

        return cleaned_data
    # --------------------------------------------------------------------------------------------------------

# Login form:
class LoginForm(forms.Form):
    # username form: foydalanuvchi username ni kiritish uchun form, maksimal 50 ta simvol kiritish mumkin;
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Foydalanuvchi nomi"
    )
    # --------------------------------------------------------------------------------------------------------
    # password form: foydalanuvchi password kiritish uchun form; password 8 ta simvoldan kam 15 ta simvoldan ko`p bo`lmasligi kerak;
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg" # class:
        }),
        label="Parol" # label:
    )
# --------------------------------------------------------------------------------------------------------

# Comment form:
class CommentForm(forms.Form):
    # text form: Foydalanuvchi biror bir gul haqidagi postga izoh qoldirishi uchun form; kament uzunligi 1000 ta simvoldan oshmasligi kerak;
    text = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={
            'placeholder': "Koment uchun joy", # placeholder: 
            'class': "form-control", # class:
            'rows': 3, # rows:  
            'style': 'resize: none;', # style:
        }),
        label="Koment", # label:
    )

    def save(self, comment, user, flower):
        comment.objects.create(
            text=self.cleaned_data.get('text'),
            author=user,
            flower=flower
        )

    def update(self, value):
        value.text = self.cleaned_data.get('text')
        value.save()
# --------------------------------------------------------------------------------------------------------