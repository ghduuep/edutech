from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import AlunoViewSet, TurmaViewSet, MatriculaViewSet, NotaViewSet, AlunoMediaView

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='alunos')
router.register('turmas', TurmaViewSet, basename='turmas')
router.register('matriculas', MatriculaViewSet, basename='matriculas')
router.register('notas', NotaViewSet, basename='notas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/media/', AlunoMediaView.as_view(), name='aluno-media'),                                                                                                                                                       
]
