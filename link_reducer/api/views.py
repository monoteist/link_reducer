from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from link_reducer.models import Link
from .serializers import LinkSerializer


class CreateShortLinkAPI(APIView):
    def post(self, request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatisticsAPI(APIView):
    def get(self, request):
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)
