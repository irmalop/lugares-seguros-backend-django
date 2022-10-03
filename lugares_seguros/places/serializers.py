from rest_framework import serializers
from places.models import Place
from comments.serializers import CommentPlaceListSerializer
from comments.models import Comment

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class PlaceListCommentSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'comment',
        )
    def get_comment(self, obj):
        selected_comment=Comment.objects.filter(place__id=obj.id)
        return CommentPlaceListSerializer(selected_comment, many=True).data