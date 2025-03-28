from django.urls import path
from .views import listar_pessoas, pessoa_por_id, pessoa_aleatoria

urlpatterns = [
    path('pessoas/', listar_pessoas, name='listar_pessoas'),
    path('pessoas/id/<int:id>/', pessoa_por_id, name='pessoa_por_id'),
    path('pessoas/random/', pessoa_aleatoria, name='pessoa_aleatoria'),
]