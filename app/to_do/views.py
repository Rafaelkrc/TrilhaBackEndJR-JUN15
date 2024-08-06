from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.to_do.serializers import ToDoSerializer
from app.to_do.models import ToDo


class ToDoCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
