from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Maktab
from .serializers import MaktabSerializer

class MaktabAPI(APIView):
    def get(self, request):
        malumot = Maktab.objects.all()
        serializer = MaktabSerializer(malumot, many=True)
        return Response(serializer.data)

    def post(self, request):
        kop_narsami = isinstance(request.data, list)
        serializer = MaktabSerializer(data=request.data, many=kop_narsami)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)    