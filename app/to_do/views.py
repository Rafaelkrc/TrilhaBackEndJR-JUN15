from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from app.to_do.serializers import ToDoSerializer
from app.to_do.models import ToDo
from app.to_do.permissions import IsAuthorOrReadOnly



class ToDoCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return ToDo.objects.filter(creator=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ToDoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return ToDo.objects.filter(creator=self.request.user)
