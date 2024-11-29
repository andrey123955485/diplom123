from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

# Страница добавление товара
from django.shortcuts import render, redirect
from .models import Item
from django.contrib import messages

def add_item(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        type = request.POST.get('type')
        weight = request.POST.get('weight')
        quantity = request.POST.get('quantity')
        image = request.FILES.get('image')  # Получаем изображение из формы

        # Создание нового товара в базе данных
        Item.objects.create(
            name=name,
            price=price,
            category=category,
            type=type,
            weight=weight,
            quantity=quantity,
            image=image  # Сохраняем изображение
        )

        # Сообщение об успешном добавлении
        messages.success(request, "Товар успешно добавлен!")

        return redirect('add_item')

    return render(request, 'core/add_item.html')
# Страница добавление товара
