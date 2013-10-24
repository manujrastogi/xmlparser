# Create your views here.
from django.shortcuts import HttpResponse, render_to_response
from django.template import RequestContext
from lxml import etree
from django.contrib.auth.models import User
from .forms import *
from .models import *


def index(request):
    '''
    Home page
    '''
    if request.method == 'POST':
        try:
            # creating new user
            user, created = User.objects.get_or_create(username=request.POST['username'],
                                                   email=request.POST['email'],
                                                   password=request.POST['password'],
                                                   first_name=request.POST['name'],
                                                   last_name=request.POST['last_name'])
        except Exception as e:
            return HttpResponse(e)
        # creating xml using lxml
        root_node = etree.Element('information')  # creating root node name -> information
        root_node.attrib['username'] = user.username  # adding attribute to it -> <information username='xyz'/>
        root_node.attrib['xmlns'] = "http://myspace.com/manujrastogi#"
        phone = etree.Element('phone')  # adding child node
        phone.text = str(request.POST['phone'])  # childnode text <phone>text</phone>
        food = etree.Element('food')
        food.text = str(request.POST['food'])
        root_node.append(phone)  # append that child node to root node
        root_node.append(food)
        xml = etree.tostring(root_node)
        '''
        <information username="xyz" ns="http://myspace.com/manujrastogi#">
            <phone>9999999999</phone>
            <food>Burger</food>
        </information>
        '''
        # Save xml
        basicinfo = BasicInfo.objects.create(user=user, xml=xml)

    form = BasicInfoForm()
    return render_to_response('index.html', {'form':form}, context_instance=RequestContext(request))


def getData(request):
    '''
    List Data
    '''
    _tag = lambda tag_name: "{%s}%s" % ("http://myspace.com/manujrastogi#", tag_name)

    infos = BasicInfo.objects.all()
    data = {}
    for info in infos:
        root = etree.XML(info.xml)  # converts xml string into xml object
        phone = root.findtext(_tag('phone'))
        food = root.findtext(_tag('food'))
        data['username'] = info.user.username
        data['phone'] = phone
        data['food'] = food
    return render_to_response('list.html', {'data':data}, context_instance=RequestContext(request))

