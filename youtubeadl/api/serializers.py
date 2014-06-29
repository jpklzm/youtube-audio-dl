from rest_framework import serializers

from api.models import YouTube, ActivityLog


class YouTubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTube


class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog