from rest_framework import serializers
from escola.models import Aluno, Matricula, Turma
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