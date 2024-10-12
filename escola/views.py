from rest_framework import viewsets, serializers
from escola.models import Aluno, Matricula, Turma, Nota
from escola.serializers import AlunoSerializer, TurmaSerializer, MatriculaSerializer, NotaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all().order_by('nome')
    serializer_class = AlunoSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all().order_by('periodo')
    serializer_class = TurmaSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by('data_matricula')
    serializer_class = MatriculaSerializer

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all().order_by('nota')
    serializer_class = NotaSerializer

