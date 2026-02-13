from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Elshod
from .serializers import ElshodSerializer

class ElshodAPI(APIView):
    def get(self, request):
        malumot = Elshod.objects.all()
        serializer = ElshodSerializer(malumot, many=True)
        return Response(serializer.data)

    def post(self, request):
        kop_narsami = isinstance(request.data, list)
        serializer = ElshodSerializer(data=request.data, many=kop_narsami)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)    