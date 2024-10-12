from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.nome

class Periodo(models.Model):
    periodo = models.IntegerField()

    def __str__(self):
        return f'{self.periodo}'

class Turma(models.Model):
    TURMAS = (
            ('M', 'Medio'),
            ('F2', 'Fundamental 2'),
            ('F1', 'Fundamental 1'),
        )

    turma = models.CharField(max_length=2, choices=TURMAS, default='F1')
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.turma}'
    
class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, blank=True, null=True)
    data_matricula = models.DateTimeField(auto_now_add=True)
    data_encerramento_matricula = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Aluno: {self.aluno}\nTurma: {self.turma}\nDesde: {self.data_matricula}'


