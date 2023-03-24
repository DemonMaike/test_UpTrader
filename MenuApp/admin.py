from django.contrib import admin
from .models import Menu, Item, Subitem


class MenuAdmin(admin.ModelAdmin):
    title = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class ItemAdmin(admin.ModelAdmin):
    title = ('title',)
    prepopulated_fields = {'slug': ('title',) }

class SubitemAdmin(admin.ModelAdmin):
    title = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Menu, MenuAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Subitem, SubitemAdmin)

