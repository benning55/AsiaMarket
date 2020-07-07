from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def get_information(request, *args, **kwargs):
    """
    get all information
    """
    if request.method == 'GET':

        if kwargs.get('key') is None:
            return Response({"price": "BEN"}, status=status.HTTP_200_OK)
        else:
            key = kwargs.get('key')
            