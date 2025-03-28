from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import cloudinary
import cloudinary.uploader
from cloudinary.models import CloudinaryField

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)  # Armazena no Cloudinary

    def __str__(self):
        return self.nome

# Signal para deletar a imagem do Cloudinary quando o objeto for excluído
@receiver(post_delete, sender=Pessoa)
def delete_image(sender, instance, **kwargs):
    if instance.image:  # Verifica se há uma imagem associada
        cloudinary.uploader.destroy(instance.image.public_id)  # Deleta do Cloudinary