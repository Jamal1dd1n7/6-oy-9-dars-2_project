from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.handlers.wsgi import WSGIRequest
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from datetime import datetime
from .models import *
from .forms import *

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
    comments = Comment.objects.filter(flower_id=flower_id)
    context = {
        'flower': flower,
        'title': flower.name,
        'form': CommentForm(),
        'comments': comments,
        'current_year': datetime.now().year
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

def comment_save(request: WSGIRequest, flower_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(data=request.POST)
            flower = get_object_or_404(Flower, pk=flower_id)
            if form.is_valid():
                form.save(Comment, request.user, flower)
                messages.success(request, "Izoh muvaffaqiyatli qo'shildi.")
                return redirect('flower_detail', flower_id=flower_id)
    else:
        messages.error(request, "Iltimos, tizimga kirishingiz kerak.")
        return redirect('login')

def comment_delete(request: WSGIRequest, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.user == comment.author or request.user.is_superuser:
            flower_id = comment.flower.id
            comment.delete()
            messages.success(request, "Izoh muvaffaqiyatli o'chirildi!")
            return redirect('flower_detail', flower_id=flower_id)


def comment_update(request: WSGIRequest, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_id)
        flower_id = comment.flower.id
        if request.user == comment.author or request.user.is_superuser:
            if request.method == 'POST':
                form = CommentForm(data=request.POST)
                if form.is_valid():
                    form.update(comment)

                    messages.success(request, "Izoh muvaffaqiyatli o'zgartirildi.")
                    return redirect('flower_detail', flower_id=flower_id)

            else:
                form = CommentForm(initial={'text': comment.text})

            context = {
                'flower': comment.flower,
                'form': form,
                'update': True,
                'comment': comment,
                'comments': Comment.objects.filter(flower_id=flower_id)
            }

            return render(request, 'flower.html', context)

    else:
        messages.error(request, "Iltimos, tizimga kirishingiz kerak.")
        return redirect('login')
    
def add_type(request: WSGIRequest):

    if request.method == 'POST':
        form = TypeForm(data=request.POST)
        if form.is_valid():
            post = Type1.objects.create(**form.cleaned_data)
            print(post, "qo'shildi!")

    form = TypeForm()
    context = {
        "form": form
    }
    return render(request, 'add_type.html', context)

def update_type(request: WSGIRequest, type_id):
    types = get_object_or_404(Type1, pk=type_id)

    if request.method == 'POST':
        form = TypeForm(data=request.POST, files=request.FILES)
        if form.is_valid():

            if Type1.objects.filter(name=form.cleaned_data.get('name')).exists():
                messages.success(request, "Ma'lumot o'zgartirilmadi. Bunday ma'lumot allaqachon qo'shilgan.")
                return redirect('home')

            types.name = form.cleaned_data.get('name')
            types.save()

            messages.success(request, "Ma'lumot muvaffaqiyatli o'zgartirildi.")
            return redirect('home')

    forms = TypeForm(initial={
        'name': types.name
    })

    context = {
        'forms': forms,
        'current_year': datetime.now().year
    }

    return render(request, 'addType.html', context)

def delete_type(request, type_id):
    type = get_object_or_404(Type1, pk=type_id)
    type.delete()
    messages.success(request, "Ma'lumot muvaffaqiyatli o'chirildi.")
    return redirect('home')

def update_flower(request: WSGIRequest, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)

    if request.method == 'POST':
        form = FlowerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            flower.name = form.cleaned_data.get('name')
            flower.photo = form.cleaned_data.get('photo')
            flower.type1 = form.cleaned_data.get('type')
            flower.color = form.cleaned_data.get('color')
            flower.price = form.cleaned_data.get('price')
            flower.production_date = form.cleaned_data.get('production_date')
            flower.save()

            messages.success(request, "Ma'lumot muvaffaqiyatli o'zgartirildi.")
            if flower.published:
                return redirect('flower', flower_id=flower_id)
            else:
                return redirect('home')

    forms = FlowerForm(initial={
        'name': flower.name,
        'photo':flower.photo,
        'type':flower.type1,
        'color':flower.color,
        'price':flower.price,
        'production_date':flower.production_date
    })

    context = {
        'forms': forms
    }

    return render(request, 'add_flower.html', context)

def delete_flower(request, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)
    flower.delete()

    messages.success(request, "Ma'lumot muvaffaqiyatli o'chirildi.")
    return redirect('home')

def register(request: WSGIRequest):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            User.objects.create_user(username, email, password)

            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
            return redirect('login')
    else:
        form = RegisterForm()


    context = {
        'forms': form,
        'current_year': datetime.now().year
    }

    return render(request, 'auth/sign_up.html', context)



def loginPage(request: WSGIRequest):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Tizimga muvaffaqiyatli kirdingiz!")
                return redirect('home')
            else:
                messages.error(request,
                               "Kiritilgan foydalanuvchi nomi yoki parol noto`g`ri. Iltimos, qayta tekshirib ko`ring.")

    context = {
        'forms': LoginForm(),
        'current_year': datetime.now().year
    }

    return render(request, 'auth/login.html', context)

def logoutPage(request: WSGIRequest):
    logout(request)
    messages.success(request, "Tizimdan muvaffaqiyatli chiqdingiz!")
    return redirect('home')