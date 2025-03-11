from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'




class Contact(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Primeiro Nome', help_text='Texto de ajuda')
    last_name = models.CharField(blank=True, max_length=255, verbose_name='Sobrenome')
    phone = models.CharField(max_length=255, verbose_name='Telefone')
    email = models.EmailField(blank=True, max_length=255, verbose_name='E-mail')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Data de Criação')
    description = models.TextField(blank=True, verbose_name='Descrição')
    show = models.BooleanField(default=True, verbose_name='Mostrar')
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Categoria')
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Criador')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

