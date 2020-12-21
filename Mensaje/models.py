from django.db import models
from django.conf import settings
from django.db.models import Q


User = settings.AUTH_USER_MODEL

class ArbolManager(models.Manager):

    def por_usuario(self, usuario):
        buscar_query  = Q(primero=usuario) | Q(segundo=usuario)
        buscar_query2 = Q(primero=usuario) & q(segundo=usuario)
        qs = self.get_queryset().filter(buscar_query).exclude(buscar_query2).distinct()
        return qs 
    
    def obtener_o_crear_nuevo(sekf, usuario, otro_usuario): #get_or_create
        username = usuario.username
        if username == otro_usuario:
            return None
        buscar_query  = Q(primero__username=username) & Q(segundo__username=otro_usuario)
        buscar_query2 = Q(primero__username=otro_usuario) & Q(segundo__username=username)
        qs = self.get_queryset().filter(buscar_query | buscar_query2).distinct()

        if qs.count() == 1:
            return qs.first(), False
        elif qs.count() > 1:
            return qs.order_by('tiempo').first(), False

        else:
            Klass = usuario.__class__
            usuario2 = Klass.objects.get(username=otro_usuario)
            if usuario != usuario2:
                obj = self.model(
                    primero=usuario,
                    segundo=usuario2
                )
                obj.save()
                return obj, True 
            return None, False

class Arbol(models.Model):
    primero    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_arbol_primero")
    segundo    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_arbol_segundo")
    actualizar = models.DateTimeField(auto_now=True)
    tiempo     = models.DateTimeField(auto_now_add=True)

    objects = ArbolManager()

class ChatMensaje(models.Model):
    arbol   = models.ForeignKey(Arbol, null=True, blank=True, on_delete=models.SET_NULL)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="envia")
    mensaje = models.TextField()
    tiempo  = models.DateTimeField(auto_now_add=True)