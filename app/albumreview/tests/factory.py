from albumreview.models import Musician, Album


class MusicianFactory(object):
    def __init__(self):
        self.counter = 0

    def __call__(self, first_name=None, last_name=None, instrument=None):
        if first_name is None:
            first_name = 'Foo%s' % self.counter
        if last_name is None:
            last_name = 'Bar%s' % self.counter
        if instrument is None:
            instrument = 'Blowfish%s' % self.counter

        musician = Musician.objects.create(
            first_name=first_name,
            last_name=last_name,
            instrument=instrument
        )
        self.counter +=1
        return musician


class AlbumFactory(object):
    def __init__(self):
        self.counter = 0

    def __call__(self, musician, name=None, release_date=None, num_stars=None):
        if name is None:
            name = 'Album%s' % self.counter
        if release_date is None:
            release_date = '2014-03-03'
        if num_stars is None:
            num_stars = 5

        album = Album.objects.create(
            musician=musician,
            name=name,
            release_date=release_date,
            num_stars=num_stars
        )
        self.counter += 1
        return album
