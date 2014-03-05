from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Album(models.Model):
    musician = models.ForeignKey(Musician, related_name='albums')
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __unicode__(self):
        return self.name
