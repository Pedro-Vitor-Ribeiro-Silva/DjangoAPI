from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Pessoa
from .serializers import PessoaSerializer
import random
from django.http import HttpResponse

def index(request):
    return HttpResponse('API ON')

@api_view(['GET'])
def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    serializer = PessoaSerializer(pessoas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pessoa_por_id(request, id):
    try:
        pessoa = Pessoa.objects.get(id=id)
        serializer = PessoaSerializer(pessoa )
        return Response(serializer.data)
    except Pessoa.DoesNotExist:
        return Response({'mensagem': 'ERRO! Usuário não encontrado'}, status=404)

@api_view(['GET'])
def pessoa_aleatoria(request):
    pessoas = list(Pessoa.objects.all())
    if pessoas:
        pessoa = random.choice(pessoas)
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)
    return Response({'mensagem': 'Nenhuma pessoa encontrada'}, status=404)


