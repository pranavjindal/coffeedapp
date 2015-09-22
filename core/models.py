import os
import uuid
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Avg
from geoposition.fields import GeopositionField

RATING_CHOICES = (
    (0, 'None'),
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),
)

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)

# Create your models here.
class Location(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	position = GeopositionField(null=True, blank=True)
	hours = models.TextField(null=True, blank=True)
	image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse(viewname="location_detail", args=[self.id])

	def get_avg_rating(self):
		avg_rating = self.review_set.all().aggregate(Avg('rating'))['rating__avg']
		if avg_rating == None:
			return avg_rating
		else:
			return int(avg_rating)

	def get_reviews(self):
		return self.review_set.all()


class Review(models.Model):
	location = models.ForeignKey(Location)
	user = models.ForeignKey(User)
	description = models.TextField(null=True, blank=True)
	rating = models.IntegerField(choices = RATING_CHOICES, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

