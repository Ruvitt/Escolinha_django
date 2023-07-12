from django.urls import path
from .views import TurmaCreate, AtividadeCreate
from .views import TurmaUpdate, AtividadeUpdate

urlpatterns = [ 
    path('cadastrar/turma/', TurmaCreate.as_view(), name='cadastrar-turma'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('editar/turma/<int:pk>/', TurmaUpdate.as_view(), name='editar-turma'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),
]