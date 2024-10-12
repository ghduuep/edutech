from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import AlunoViewSet, TurmaViewSet, MatriculaViewSet, PeriodoViewSet

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='alunos')
router.register('turmas', TurmaViewSet, basename='turmas')
router.register('matriculas', MatriculaViewSet, basename='matriculas')
router.register('periodos', PeriodoViewSet, basename='periodos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
