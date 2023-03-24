from django.db import models
from django.shortcuts import reverse

class Menu(models.Model):
    '''Class for working with menus'''
    title = models.CharField(verbose_name='Name for menu',max_length=255)
    slug = models.SlugField(verbose_name='Slug', max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse('menu', kwargs={'slug_menu': self.slug})
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
        ordering = ['title']

class Item(models.Model):
    '''Class for working with items'''
    title = models.CharField(verbose_name='Name of item', max_length=255)
    slug = models.SlugField(verbose_name='Slug', max_length=255, unique=True)
    sub_menu = models.ForeignKey('Menu', on_delete=models.CASCADE,
                                 verbose_name='Menu',related_name='mainmenu')

    def get_absolute_url(self):
        return reverse('item', kwargs={'slug_menu': self.sub_menu.slug, 'slug_item':self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
    
class Subitem(models.Model):
    '''Class for working with subitems'''
    title = models.CharField(verbose_name='Name of subitem', max_length=255)
    slug = models.SlugField(verbose_name='Slug', max_length=255, unique=True)
    sub_item = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name='Item', related_name='item')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('subitem', kwargs={'slug_menu': self.sub_item.sub_menu.slug, 'slug_item':self.sub_item.slug,'slug_subitem':self.slug})

    class Meta:
        verbose_name = 'Subitem'
        verbose_name_plural = 'Subitems'
