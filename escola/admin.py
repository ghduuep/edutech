from django.contrib import admin
from escola.models import Turma, Matricula, Aluno

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

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['id', 'aluno__nome', 'turma__turma', 'data_matricula', 'data_encerramento_matricula',]
    list_per_page = 20
    search_fields = ['aluno__nome', 'turma__turma', 'data_matricula', 'data_encerramento_matricula',]
    list_filter = ['aluno__nome', 'turma__turma', 'data_matricula', 'data_encerramento_matricula',]
    list_display_links = ['aluno__nome', 'turma__turma',]

admin.site.register(Matricula, MatriculaAdmin)

