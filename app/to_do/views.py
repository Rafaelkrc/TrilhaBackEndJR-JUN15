from rest_framework import generics
from app.to_do.serializers import ToDoSerializer
from app.to_do.models import ToDo


class ToDoCreateListView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
