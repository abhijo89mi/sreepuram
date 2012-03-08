from models import *
from django.conf import settings
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
import datetime

def index(request):
	settings=Settings.objects.get(id=1)
	if settings.site_offline :
		template='offline.html'

	else:
		template='main/index.html'
	context={}
	return render_to_response (template, context, context_instance=RequestContext(request))
