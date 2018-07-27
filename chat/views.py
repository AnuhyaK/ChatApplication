from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Room
from .models import OnlineUsers
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
import json
from urllib.parse import urlparse
'''from urlparse import urljoin,parse_qs,urlparse
from urlparse import urlparse'''


User = get_user_model()
        
@login_required
def index(request):

    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")
    #usersOnline = User.objects.all()
    #console.log(usersOnline)
    # Render that in the index template
    #obj_generator = serializers.json.Deserializer(request.session['json_u'])
    return render(request, "index.html", {
        "rooms": rooms	
        
     })

def userlist(request):
        '''parsed = urlparse(request)
        print(urlparse.parse_qs(parsed.query)['roomid'])
        print("Reust from load:",request)'''
    
        room_id=1
        records = OnlineUsers.objects.filter(title=room_id)
        print("Records",records)
        json_res = []
        
        print("Lent",len(records))
        for record in records:
            json_obj=record.user
            json_res.append(json_obj)
            json_stuff=json.dumps(json_res, indent=2)
            print(json_stuff)
        return HttpResponse(json_stuff,content_type='application/json')

'''def userlist_of_room2(request):
        parsed = urlparse(request)
        print(urlparse.parse_qs(parsed.query)['roomid'])
        print("Reust from load:",request)
        room_id=2
        records = OnlineUsers.objects.filter(title=room_id)
        print("Records",records)
        json_res = []
        json_stuff = []
        print("Lent",len(records))
        for record in records:
            json_obj=record.user
            json_res.append(json_obj)
            json_stuff=json.dumps(json_res, indent=2)
            print(json_stuff)
        return HttpResponse(json_stuff,content_type='application/json')'''

'''def userlist_new(request):
    #onlineuser=[]
    #onlineuser = OnlineUsers.objects.filter(user="sahithi")
        room_id=2
        data = serializers.serialize('json', OnlineUsers.objects.filter(title=room_id))
        #onlineUsers = OnlineUsers.objects.filter(title=room_id).values('user')
        #serializers.serialize('json', events)
        print("Hello World",data)
        return HttpResponse(json.dumps(data, indent= 2, sort_keys=True ))'''
        


