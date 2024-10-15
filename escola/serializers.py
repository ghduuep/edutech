from rest_framework import serializers
from escola.models import Aluno, Matricula, Turma, Nota
from escola.validators import cpf_invalido, nome_invalido

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
    
    def validate(self, dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF tem que ser valido'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome': 'O nome tem que conter apenas letras'})
        return dados

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ['nota', 'bimestre']
    
class MediaNotaSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField()
    aprovado = serializers.SerializerMethodField()

    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'media', 'aprovado']

    def get_media(self, obj):
        notas = Nota.objects.filter(aluno=obj)
        if notas.exists():
            media = sum(nota.nota for nota in notas) / len(notas)
            return round(media, 2)
        return 0.0                                                                                                                         
    
    def get_aprovado(self, obj):
        media = self.get_media(obj)
        return media >= 28