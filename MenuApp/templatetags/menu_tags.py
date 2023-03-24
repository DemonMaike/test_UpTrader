from django import template
from MenuApp.models import Menu, Item, Subitem


register = template.Library()

@register.simple_tag(name='main_menu')
def main_menu():
    """printing of menu"""
    return Menu.objects.all()
