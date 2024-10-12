from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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

class Aluno(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.nome

class Nota(models.Model):

    BIMESTRES = (
        ('1', '1 Bimestre'),
        ('2', '2 Bimestre'),
        ('3', '3 Bimestre'),
        ('4', '4 Bimestre'),
    )

    nota = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(10.00)])
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    bimestre = models.CharField(max_length=1, choices=BIMESTRES, default='1')

    def __str__(self):
        return f'{self.nota}'

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, blank=True, null=True)
    data_matricula = models.DateTimeField(auto_now_add=True)
    data_encerramento_matricula = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Aluno: {self.aluno}\nTurma: {self.turma}\nDesde: {self.data_matricula}'