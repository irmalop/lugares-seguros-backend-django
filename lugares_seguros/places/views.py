from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from places.models import Place
from places.serializers import PlaceSerializer, PlaceListCommentSerializer


class PlaceView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        places = Place.objects.all()
        print(places)
        serializer = PlaceSerializer(places, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        try:
            file = request.data['image']
            request.data['image'] = file
        except KeyError:
            file = None
        serializer = PlaceSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class PlaceSingleView(APIView):
    
    def get(self, request, id):
        place = Place.objects.filter(id=id).first()
        if place is None:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer=PlaceListCommentSerializer(place)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        place = Place.objects.get(id = id)
        serializer = PlaceSerializer(place, data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)

    def delete(self, request, id):
        place = Place.objects.get(id = id)
        place.delete()
        return Response({"message": "Lugar eliminado exitosamente"}, status = status.HTTP_204_NO_CONTENT)