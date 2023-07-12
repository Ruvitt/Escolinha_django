from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Turma, Atividade

# Create
class TurmaCreate(CreateView):
    model = Turma
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('inicio')

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'turma']
    template_name = 'form.html'
    success_url = reverse_lazy('inicio')

# update
class TurmaUpdate(UpdateView):
    model = Turma
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('inicio')

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'turma']
    template_name = 'form.html'
    success_url = reverse_lazy('inicio')