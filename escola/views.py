from rest_framework import viewsets, serializers
from escola.models import Aluno, Matricula, Turma, Periodo
from escola.serializers import AlunoSerializer, TurmaSerializer, MatriculaSerializer, PeriodoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all().order_by('nome')
    serializer_class = AlunoSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


