# Create your views here.

from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import MethodNotAllowed

from .models import FieldWorker
from .serializers import FieldWorkerSerializer


class FieldWorkerViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """
    Create, list, partial update and destroy FieldWorker
    """
    queryset = FieldWorker.objects.order_by('id')
    serializer_class = FieldWorkerSerializer
    permission_classes = [AllowAny]

    def update(self, *args, **kwargs):
        raise MethodNotAllowed("POST", detail="Use PATCH")

    def partial_update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)

