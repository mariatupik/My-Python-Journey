
import time

from .serializers import ItemSerializer, OrderSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from cloudipsp import Api, Checkout


class ItemsPage(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class OrderAdd(APIView):
    def post(self, req):
        order = OrderSerializer(data=req.data)

        if order.is_valid():
            order.save()

            api = Api(merchant_id=1396424,
                      secret_key='test')
            checkout = Checkout(api=api)
            data = {
                "currency": "USD",
                "amount": int(req.data['summa']) * 100,
                "order_desc": "Оплата товарів",
                "order_id": str(time.time())
            }
            url = checkout.url(data).get('checkout_url')

            return Response({'result': 'Пару секунд...', 'url': url})

        return Response({'result': 'Помилка в формі'})


class ItemEdit(APIView):
    def put(self, req, *args, **kwargs):
        item = Item.objects.filter(slug=kwargs["slug"]).first()

        if not item:
            return Response(
                {"error": "Товар не знайдено"},
                status=status.HTTP_404_NOT_FOUND
            )

        item.image = req.data.get("image", item.image)
        item.title = req.data.get("title", item.title)
        item.desc = req.data.get("desc", item.desc)
        item.price = req.data.get("price", item.price)
        item.save()

        return Response({"result": "Товар оновлено"}, status=status.HTTP_200_OK)