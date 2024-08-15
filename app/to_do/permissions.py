from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Permissão personalizada para garantir que apenas o autor da tarefa
    possa visualizá-la, atualizá-la ou excluí-la.
    """

    def has_object_permission(self, request, view, obj):
        # Permissão é concedida apenas se o usuário autenticado for o autor
        return obj.creator == request.user
