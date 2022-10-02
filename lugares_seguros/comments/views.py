from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer


class CommentView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class CommentSingleView(APIView):
    def delete(self, request, pk):
        place = get_object_or_404(Comment, pk=pk)
        place.delete()
        return Response('Comentario eliminado', status=status.HTTP_204_NO_CONTENT)
