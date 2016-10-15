from django.shortcuts import render
from django.http import HttpResponse
from models import *
from django.contrib.auth.models import *
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
#from django.template.loader import render_to_string
import json
from django.shortcuts import render_to_response
from django.contrib.auth.hashers import make_password

def users(request):
    _id = request.GET
    objs = User.objects.filter(**eval(json.dumps(dict([i for i in _id.dict().items() if i[0] != '_'])))) if _id else  User.objects.all()
    data = [ {'id': i['pk'], 'fields': {k: j for k, j in i['fields'].iteritems() if k not in ('password')}} for i in json.loads(serializers.serialize('json', objs))]
    return HttpResponse(json.dumps({'data': data}), content_type="application/json")

def add_user(request):
    _id = request.GET
    try:
        user = User.objects.create(username=_id.get('username',''))
    except:
	return HttpResponse("User Already existed")

    user.password = make_password(_id.get('password'))
    user.email = _id.get('email')
    user.save()
    return HttpResponse("User Added Scueessfully")
    #objs = User.objects.get_or_create(**eval(json.dumps(dict([i for i in _id.dict().items() if i[0] != '_'])))

def update_or_delete(request):
    _id = request.GET
    if _id.get('method', '') == 'delete':
        User.objects.filter(id=_id['id']).delete()
    else:
        try:
	    obj = User.objects.filter(id=_id['id']).update(**eval(_id['fields']))
        except KeyError:
	    return HttpResponse("Key Error") 
        except:
	    return HttpResponse("Error Occured")      
    return HttpResponse("Success")

def home(request):
    return render_to_response('view_data.html')

def adduser(request):
    return render_to_response('base.html')

def deleteuser(request):
    return render_to_response('delete_data.html')

# Create your views here.
