from rest_framework import permissions


class IsAdminOrSelf(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Permitir GET para admins ou para o próprio usuário
            return request.user.is_staff or view.kwargs.get('pk') == str(request.user.id)
        return request.user.is_staff  # Apenas admins para outros métodos

    def has_object_permission(self, request, view, obj):
        # Checar permissões para operações específicas do objeto
        if request.method in permissions.SAFE_METHODS:
            return True  # Admins e o próprio usuário podem acessar
        return obj.id == request.user.id or request.user.is_staff
