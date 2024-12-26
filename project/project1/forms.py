from django import forms

from .models import Type1, Flower


class FlowerForm(forms.Form):
    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        "placeholder": "Nomi",
        "class": "form-control"
    }), label='Nomi')
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "form-control"
    }))
    type1 = forms.ModelChoiceField(queryset=Type1.objects.all(), widget=forms.Select(attrs={
        "class": "form-select"
    }))
    color = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        "placeholder": "Rangi",
        "class": "form-control"
    }), required=False)
    price = forms.IntegerField(widget=forms.TextInput(attrs={
        "placeholder": "Narxi"
    }))
    production_date =forms.TimeField(widget=forms.TimeInput(attrs={
        "placeholder": "Sotuvga chiqarilgan vaqti",
        "class": "form-control"
    }))


class CourseForm(forms.Form):
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        "placeholder": "Nomi",
        "class": "form-control"
    }), label='Nomi')
    teacher = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        "placeholder": "O`qituvchi",
        "class": "form-control"
    }), label='O`qituvchi')
    course_type = forms.CharField(max_length=250,widget=forms.TextInput(attrs={
        "placeholder": "Kurs turi",
        "class": "form-control"
    }), required=False)
    created_at =forms.TimeField(widget=forms.TimeInput(attrs={
        "placeholder": "Kurs ochilgan vaqt",
        "class": "form-control"
    }))
    student_count = forms.IntegerField(widget=forms.NumberInput(attrs={
        "placeholder": "O`quvchi soni",
        "class": "form-control"
    }))



# class PostForm(forms.Form):
    # title = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
    #     "placeholder": "Nomi",
    #     "class": "form-control"
    # }), label='Nomi')
    # content = forms.CharField(widget=forms.Textarea(attrs={
    #     "placeholder": "Matni",
    #     "class": "form-control"
    # }), required=False)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
    #     "class": "form-select"
    # }))
    # published = forms.BooleanField(widget=forms.CheckboxInput(attrs={
    #     "class": "form-check-input",
    #     "checked": "checked"
    # }))