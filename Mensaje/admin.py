from django.contrib import admin

from .models import ChatMensaje, Arbol

class ChatMensaje(admin.TabularInline):
    model = ChatMensaje

class ArbolAdmin(admin.ModelAdmin):
    inlines = [ChatMensaje]
    class Meta:
        model = Arbol

admin.site.register(Arbol, ArbolAdmin)