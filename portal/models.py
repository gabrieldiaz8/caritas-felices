from django.db import models

class Campaign(models.Model):
    class Estado(models.TextChoices):
        ACTIVA = 'ACTIVA', 'Activa'
        INACTIVA = 'INACTIVA', 'Inactiva'
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        FINALIZADA = 'FINALIZADA', 'Finalizada'
    
    nombre = models.CharField(max_length=255, default="")
    contenido = models.TextField(default="")
    estado = models.CharField(
        max_length=50, 
        choices=Estado.choices,
        default=Estado.PENDIENTE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True) 

    @classmethod
    def obtener_activas(cls):
        return cls.objects.filter(estado=cls.Estado.ACTIVA, deleted_at__isnull=True)

    def __str__(self):
        return self.nombre
