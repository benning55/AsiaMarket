from requests.auth import HTTPBasicAuth
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from core.models import Util
from utils.serializers import UtilSerializer
import requests


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


@api_view(['POST', ])
@permission_classes([AllowAny, ])
def klarna_shoot(request, *args, **kwargs):
    """
    Shoot klarna api
    """
    if request.method == 'POST':
        data = request.data
        print(data)
        mock_data2 = {
            "purchase_country": "DE",
            "purchase_currency": "EUR",
            "locale": "en-DE",
            "order_amount": 50000,
            "order_tax_amount": 4545,
            "order_lines": [
                {
                    "type": "physical",
                    "reference": "19-402-USA",
                    "name": "Red T-Shirt",
                    "quantity": 5,
                    "quantity_unit": "pcs",
                    "unit_price": 10000,
                    "tax_rate": 1000,
                    "total_amount": 50000,
                    "total_discount_amount": 0,
                    "total_tax_amount": 4545
                }
            ],
            "merchant_urls": {
                "terms": "https://www.example.com/terms.html",
                "checkout": "https://www.example.com/checkout.html?order_id={checkout.order.id}",
                "confirmation": "https://www.example.com/confirmation.html?order_id={checkout.order.id}",
                "push": "https://www.example.com/api/push?order_id={checkout.order.id}"
            }
        }
        mock_data = {
            "locale": "en-DE",
            "order_amount": 2500,
            "order_lines": [
                {
                    "name": "Egg",
                    "quantity": 1,
                    "total_amount": 2500,
                    "unit_price": 2500
                }
            ],
            "purchase_country": "DE",
            "purchase_currency": "EUR"
        }
        url = 'https://api.klarna.com/payments/v1/sessions'
        response = requests.post(url, auth=('K765595_8b663369197a', 'U7N5Lb2T2bK5Qthv'), json=mock_data)
        return Response(response, status=response.status_code)

