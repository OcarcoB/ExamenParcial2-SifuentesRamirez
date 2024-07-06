from django.urls import path
from .views import (
TareasID,
TareasNoResueltas,
TareasNoResueltasUserID,
TareasResueltasUserID,
TareasTitulos,
TareasUserID,
TareasResueltas,
)

urlpatterns = [
    
    path('tareas/ids/', TareasID.as_view(), name='tareas-id'),
    path('tareas/titulos/', TareasTitulos.as_view(), name='tareas-titulos'),
    path('tareas/noresueltas/', TareasNoResueltas.as_view(), name='tareas-no-resueltas'),
    path('tareas/resueltas/', TareasResueltas.as_view(), name='tareas-resueltas'),
    path('tareas/user_ids/', TareasUserID.as_view(), name='tareas-user-id'),
    path('tareas/resueltas/user_ids/', TareasResueltasUserID.as_view(), name='tareas-resueltas-user-id'),
    path('tareas/noresueltas/user_ids/', TareasNoResueltasUserID.as_view(), name='tareas-no-resueltas-user-id'),
]
