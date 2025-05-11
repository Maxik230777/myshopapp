from .serializers import ItemSerializer, OrderSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item

# Create your views here.
class ItemsPage(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class OrderAdd(APIView):
    def post(self, req):

        order = OrderSerializer(data=req.data)

        if order.is_valid():
            order.save()
            # если форма корректная
            return Response({'result': 'Заказ оформлен!'})
        # если не корректная
        return Response({'result': 'Ошибка в форме'})

# class ItemEdit(APIView):
#     def put(self, req, *args, **kwargs):
#         print(req.data)
#
#         editItem = Item.objects.filter(slug=kwargs["slug"])
#
#         if editItem.is_valid():
#             editItem.save()
#             # если форма корректная
#             return Response({'result': 'Изменения сохранены'})
#
#         # если не корректная
#         return Response({'result': 'Форма не valid '})

class ItemEdit(APIView):
    def put(self, req, *args, **kwargs):
        item = Item.objects.filter(slug=kwargs['slug']).first()
        item.image = req.data['image'] # подставляем новые данные
        item.title = req.data['title']
        item.desc = req.data['desc']
        item.price = req.data['price']
        item.save() # сохраняем товар

        return Response({'result': 'Done'})