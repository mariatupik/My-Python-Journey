from django.db import models


class Item(models.Model):
    slug = models.SlugField('Унікальна назва', unique=True)
    title = models.CharField('Назва товару', max_length=200)
    image = models.CharField('Фото товару', max_length=200)
    desc = models.TextField('Опис товару')
    price = models.DecimalField('Ціна', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField('Им\'я клієнта', max_length=200)
    surname = models.CharField('Прізвище клієнта', max_length=200)
    email = models.CharField('Email', max_length=200)
    phone = models.CharField('Телефон', max_length=200)
    basket = models.TextField('Корзина товарів')

    def __str__(self):
        return self.name + ' ' + self.surname + ' (' + self.phone + ')'
