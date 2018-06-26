from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from memorization.models import Info, User, Picture, SensorData, Log
from memorization.serializers import InfoSerializer, UserSerializer, PictureSerializer, SensorDataSerializer, LogSerializer
from rest_framework.decorators import action, api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=True, url_path='pictures', url_name='pictures')
    def pictures(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            pictures = Picture.objects.filter(user_id=pk)
            serializer = PictureSerializer(pictures, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class InfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Infos to be viewed or edited.
    """
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class PictureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Pictures to be viewed or edited.
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class SensorDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SensorDatas to be viewed or edited.
    """
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


class LogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Logs to be viewed or edited.
    """
    queryset = Log.objects.all()
    serializer_class = LogSerializer