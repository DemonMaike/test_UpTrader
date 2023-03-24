from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def main(request):
    '''View for looking page with menus'''
    return render(request, 'MenuApp/base.html')

def menu(request, slug_menu):
    context = {'slug_menu': slug_menu}
    return render(request, 'MenuApp/base.html', context )


def item(request, slug_menu, slug_item):
    context = {'slug_menu': slug_menu, 'slug_item': slug_item}
    return render(request, 'MenuApp/base.html', context)

def subitem(request,slug_menu, slug_item, slug_subitem):
    context = {'slug_menu': slug_menu, 'slug_item': slug_item,'slug_subitem': slug_subitem}
    return render(request, 'MenuApp/subitem.html', context)