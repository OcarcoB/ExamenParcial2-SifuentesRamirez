from rest_framework import generics
from .models import Todo
from .serializers import (
    TareaIDSerializer,
    TareaSerializer,
    TareaTituloSerializer,
    TareaUserIDSerializer,
)

class TareasID(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TareaIDSerializer

class TareasTitulos(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TareaTituloSerializer

class TareasNoResueltas(generics.ListAPIView):
    queryset = Todo.objects.filter(is_completed=False)
    serializer_class = TareaTituloSerializer

class TareasResueltas(generics.ListAPIView):
    queryset = Todo.objects.filter(is_completed=True)
    serializer_class = TareaTituloSerializer

class TareasUserID(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TareaUserIDSerializer

class TareasResueltasUserID(generics.ListAPIView):
    queryset = Todo.objects.filter(is_completed=True)
    serializer_class = TareaUserIDSerializer

class TareasNoResueltasUserID(generics.ListAPIView):
    queryset = Todo.objects.filter(is_completed=False)
    serializer_class = TareaUserIDSerializer
