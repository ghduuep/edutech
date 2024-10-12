from django.contrib import admin
from escola.models import Turma, Matricula, Aluno, Periodo

class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cpf', 'email',]
    list_display_links = ['id', 'nome',]
    list_per_page = 20
    search_fields = ['nome', 'cpf', 'email',]

admin.site.register(Aluno, AlunoAdmin)

class TurmaAdmin(admin.ModelAdmin):
    list_display = ['id', 'turma', 'periodo',]
    list_display_links = ['id', 'turma',]

admin.site.register(Turma, TurmaAdmin)

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'periodo']
    list_display_links = ['periodo',]
    search_fields = ['periodo']
    list_filter = ['periodo']
    list_per_page = 10

admin.site.register(Periodo, PeriodoAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['id', 'aluno__nome', 'turma__turma', 'data_matricula', 'data_encerramento_matricula',]
    list_per_page = 20
    search_fields = ['aluno__nome', 'turma__turma', 'data_matricula', 'data_encerramento_matricula',]
    list_filter = ['aluno__nome', 'turma__turma', 'data_matricula', 'data_encerramento_matricula',]
    list_display_links = ['aluno__nome', 'turma__turma',]

admin.site.register(Matricula, MatriculaAdmin)

