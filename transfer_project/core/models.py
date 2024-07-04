from django.db import models
from django.core.files.base import ContentFile
from django.contrib.auth.models import AbstractUser
import qrcode
import io

class Cliente(models.Model):
    rut = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.rut

class Chofer(AbstractUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=False)
    patente = models.CharField(max_length=50, unique=True)
    posicion = models.IntegerField(blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Transfer(models.Model):
    chofer = models.OneToOneField(Chofer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Transfer de {self.chofer.nombre} {self.chofer.apellido}"

class Ticket(models.Model):
    status = models.BooleanField(default=True)
    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return f"Ticket {self.id} - Cliente: {self.cliente.rut} - Chofer: {self.chofer.nombre} {self.chofer.apellido}"

    def save(self, *args, **kwargs):
        qr_content = f"Ticket ID: {self.id}, Cliente: {self.cliente.rut}, Chofer: {self.chofer.nombre} {self.chofer.apellido}"
        qr_img = qrcode.make(qr_content)
        buffer = io.BytesIO()
        qr_img.save(buffer, format='PNG')
        file_name = f'ticket_qr_{self.id}.png'
        self.qr_code.save(file_name, ContentFile(buffer.getvalue()), save=False)
        super().save(*args, **kwargs)