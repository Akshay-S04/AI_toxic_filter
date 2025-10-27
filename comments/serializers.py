from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    text = serializers.CharField()
