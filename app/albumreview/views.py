from django.shortcuts import render
from rest_framework import generics

from albumreview.models import Musician
from albumreview.serializers import MusicianSerializer

def index_view(request):
    response = {
        'musicians': Musician.objects.all(),
    }
    return render(request, 'index.html', response)

class MusicianView(generics.ListAPIView):
    """
    Returns a list of all musicians.
    """
    model = Musician
    serializer_class = MusicianSerializer

class MusicianInstanceView(generics.RetrieveAPIView):
    """
    Returns a single musician.
    Also allows updating and deleting
    """
    model = Musician
    serializer_class = MusicianSerializer
