from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from core.models import Util
from utils.serializers import UtilSerializer


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def get_information(request, *args, **kwargs):
    """
    get all information
    """
    if request.method == 'GET':

        if kwargs.get('key') is None:
            return Response({"error": "please enter key on the /"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            key = kwargs.get('key')
            if Util.objects.all().count() == 0:
                return Response({"error": "There is no info data"}, status=status.HTTP_404_NOT_FOUND)
            else:
                queryset = Util.objects.all().filter(type=key)
                serializer = UtilSerializer(queryset, many=True)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
