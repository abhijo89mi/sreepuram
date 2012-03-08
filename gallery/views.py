from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from sreepuram.gallery.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def index(request):
    
    category_list   =Category.objects.all()
    context         ={'category':category_list }
    return render_to_response ('gallery/index.html', context, context_instance = RequestContext(request))
   
def gallery(request,name):
    images          =CategoryImage.objects.filter(image_category=name) 
    ic=Category.objects.get(category_name=name)
    catinfo = ic.category_description
    catname=ic.category_name
    context         ={'imageslist':images,'catinfo':catinfo,'catname':catname}
    return render_to_response ('gallery/images.html',context,context_instance=RequestContext(request))

def contact_form(request):
    comment = request.POST.get('comment', '')
    email = request.POST.get('email', '')
    name = request.POST.get('name', '')
    if comment == 'Comments':
        comment = ''
    if name == 'Name':
        name = ''
    if email == 'Email Address':
        email = ''
    if comment and email and name:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            a = form.save()
            to_return = {'message' : 'Thanks for contacting us. We should get back to you shortly.', 'success' : True }
        else:
            print form.errors
            to_return = {'message' : 'Please enter a valid email address.', 'success' : False }
    else:
        to_return = {'message' : 'Some of the required fields are missing.', 'success' : False }    
    return HttpResponse(simplejson.dumps(to_return), mimetype='application/json')    
