import json
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from albumreview.tests.factory import MusicianFactory, AlbumFactory

def fetch_url(url):
    client = Client()
    response = client.get(url)
    return json.loads(response.content)


class EndpointsTestCase(TestCase):

    def setUp(self):
        musician = MusicianFactory()
        musician = musician()
        album = AlbumFactory()
        for x in range(3):
            album(musician=musician)

    def test_musician_with_albums_list_endpoint(self):
        url = reverse('musician-list')
        response = fetch_url(url)
        self.assertEqual(len(response[0]['albums']), 3)
