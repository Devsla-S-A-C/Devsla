from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny

class FacultadViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Facultad.
    """
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer
    filterset_fields = '__all__'

    def get_permissions(self):
        """
        Asigna permisos dependiendo del método HTTP.
        """
        if self.action == 'list' or self.action == 'retrieve':  # Para GET (ver)
            permission_classes = [permissions.AllowAny]  # Permite a cualquiera ver los datos
        else:  # Para POST, PUT, PATCH, DELETE (editar o agregar)
            permission_classes = [permissions.IsAuthenticated]  # Solo los autenticados pueden modificar

        return [permission() for permission in permission_classes]


class EscuelaProfesionalViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de EscuelaProfesional.
    """
    queryset = EscuelaProfesional.objects.all()
    serializer_class = EscuelaProfesionalSerializer
    filterset_fields = '__all__'

    def get_permissions(self):
        """
        Asigna permisos dependiendo del método HTTP.
        """
        if self.action == 'list' or self.action == 'retrieve':  # Para GET (ver)
            permission_classes = [permissions.AllowAny]  # Permite a cualquiera ver los datos
        else:  # Para POST, PUT, PATCH, DELETE (editar o agregar)
            permission_classes = [permissions.IsAuthenticated]  # Solo los autenticados pueden modificar

        return [permission() for permission in permission_classes]