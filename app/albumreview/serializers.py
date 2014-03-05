from rest_framework import serializers

from albumreview.models import (
    Musician,
    Album,
)


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'name', 'release_date', 'num_stars')

class MusicianSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)

    class Meta:
        model = Musician
        fields = ('albums', 'id', 'first_name', 'last_name', 'instrument')
