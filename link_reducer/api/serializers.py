from rest_framework import serializers

from link_reducer.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ("id", "original_link", "shortened_link", "redirect_count")
