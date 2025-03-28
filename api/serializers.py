from rest_framework import serializers
from .models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()  # Adiciona um campo extra para a URL da imagem

    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'descricao', 'image_url']  # Remove o campo `image` e mantém apenas a URL

    def get_image_url(self, obj):
        if obj.image:  # Se houver uma imagem associada
            return obj.image.url  # Retorna a URL direta fornecida pelo Cloudinary
        return None  # Se não houver imagem, retorna `None`