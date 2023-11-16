from decimal import Decimal

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet
from .models import DesiredValues, Record
from .serializers import DesiredValuesSerializer, RecordSerializer


class DesiredValuesViewSet(GenericViewSet):
    queryset = DesiredValues.objects.all()
    serializer_class = DesiredValuesSerializer
    lookup_value_regex = r'\d+'
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def set(self, request, *args, **kwargs):
        serializer = DesiredValuesSerializer(instance=self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get(self, request, *args, **kwargs):
        return Response(data=self.get_object().desired_value)


class RecordViewSet(GenericViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    lookup_value_regex = r'\d+'
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def add(self, request, *args, **kwargs):
        serializer = RecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def get(self, request, *args, **kwargs):
        objects = Record.objects.filter(name=request.query_params.get('name'))
        serializer = RecordSerializer(objects, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def get_current_value(self, request, *args, **kwargs):
        objects = Record.objects.filter(name=request.query_params.get('name'))
        serializer = RecordSerializer(objects, many=True)
        if not objects.count():
            return Response(Decimal(0))
        return Response(Decimal(serializer.data[-1]['value']))
