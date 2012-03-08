from django.http import HttpResponse
from sreepuram.gallery.models import *

def main (request):
	slider_image = CategoryImage.objects.filter(image_category='Slider')
	context = { 'slider_image':slider_image }
	return context
