from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from .models import Flower, Type1
from .forms import FlowerForm

def home(request: WSGIRequest):
    type1 = Type1.objects.all()
    flowers = Flower.objects.all()
    context = {
        'flowers': flowers,
        'types': type1,
        'title': 'Gullar'
    }
    return render(request, 'intex.html', context)

def flower_by_type(request, type_id):
    flowers = get_list_or_404(Flower, type1_id=type_id)  # Ensure the correct field name
    type1 = get_object_or_404(Type1, id=type_id)  # Ensure the primary key matches
    context = {
        'flowers': flowers,
        "title": f"{type1.name}: barcha maqolalar!"
    }
    return render(request, 'type.html', context)

def flower_detail(request: WSGIRequest, flower_id):
    flower = get_object_or_404(Flower, id= flower_id)
    context = {
        'flower': flower,
        'title': flower.name
    }
    return render(request, 'flower.html', context)

def add_flower(request: WSGIRequest):

    if request.method == 'POST':
        form = FlowerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = Flower.objects.create(**form.cleaned_data)
            print(post, "qo'shildi!")

    form = FlowerForm()
    context = {
        "form": form
    }
    return render(request, 'add_flower.html', context)